# ROWNUM
* 순번
* Select 후에 결과집합을 만들어 내면서 rownum이라는 컬럼이 추가가 된다
* where절에 rownum을 이용하여 조건을 주면 다른 조건을 만족시킨 결과에 대해 조건이 반영된다
* \> \>= 인 경우 rownum은 동작하지 않는다
* rownum = 2 인 경우 처음 겸색되서 나온 결과에 rownum 1 이 붙고 결과값이 rownum = 2와 맞지 않기 때문에 버리게 되고 그 과정을 반복하면 rownum = 2는 도달 할 수 없는 값이 된다

### 페이징에 이용 할 수 있는데 밑의 예시처럼 따라 할 것
```sql
select * from ( select rownum num tableA.* from tableA) where number between 5 and 10;
```

# ROWID
* 데이터베이스 내에서 데이터 공유의 주소
* rowid는 인덱스에 저장됨
* 유일한 주소이지만 테이블의 PK처럼 사용될 수는 없다. 레코드를 삭제했다면 삭제된 레코드의 rowid는 나중에 입력되는 다른 레코드에 부여 될 수 있다.

* ROWID 의 구성
1. 데이터 오브젝트 번호 32bit (6자리)
1. DataFile 번호 10 bit (3자리)
1. Block 번호22bit (6자리)
1. Block 내 Slot 16bit (3자리)

### ROWID 보는 법
```sql
select rowid , * tableA from tableA
```
### 어떤 테이블이 몇개의 블록으로 이루어져 있는지
```sql
select count(Distinct(substr(rowid ,1 ,15))) as Block_Count from tableA;
/* 블록번호 까지 문자열을 잘라서 중복된 컬럼을 제거 후 카운트*/
```

# Oracle Hint
* 힌트는 옵티마이저 라고 해서 항상 최선의 실행계획을 수립 할 수는 없으므로 테이블이나 인덱스의 잘못된 실행계획을 개발자가 직접 바꿀 수 있도록 도와주는 것
* 사용자는 오라클 옵티마이보다 더 좋은 실행계획을 둘 수 있다
```sql
select /*+ 힌트내용 */ * from tableA
```

> ordered 힌트를 써서 from 절 이후에 나온 테이블 순서대로 조인이 일어나게끔 한다

# Nasted Loof Join
* Nasted Loof Join 은 2개 이상의 테이블에서 하나의 집합을 기준으로 순차적으로 상대방 Row를 결합하여 원하는 결과를 조합하는 방식
* 먼저 선행 테이블의 처리 범위를 하나씩 엑세스 하면서 추출된 값으로 연결한 테이블을 조인한다
* 자바 코드에서 반복문 2개 방식
* 소량의 범위처리를 할 때는 유리하지만 대량의 범위는 부하를 많이 준다
* 랜덤 엑세스에 대한 부하가 있다

> 힌트의 사용
```sql
/*+ USE_NL(table1, table2 ...) */
// Nested Loof 조인 이용

/*+ NO_USE_NL(table1, table2 ...) */
// Nested Loof 조인 이용안함

/*+ USE_NL_WITH_INDEX(table1, table2 ...) */
```

> 파라메터로서 드라이븐 테이블(비 드라이빙 테이블, 두번째 이후에 나오는 테이블을 지정) 인자 두개가 오면 자동으로 지정
>> 힌트에서 ordered 키워드가 없으면 힌트가 무시된다

# Merge Join
* 테이블을 소팅하고 병합해서 검색
* 범위 검색에 적절

```sql
/*+ USE_MERGE(table1, table2 ...) */
//소트 머지 조인 이용
```

# Hash Join
* 데이터가 적은 테이블을 메모리에 올려두고 해쉬함수를 이용해 두번째 테이블과의 조인을 시도하는 방법
```sql
/*+ USE_HASH(table1, table2 ...) */
//HASH 조인 이용
```

# Oracle Hint
## 최적화 목표 제어 힌트
* FIRST_ROWS
** 최적 응답시간을 목표로 최저 비용의 실행계획을 수립하도록 유도한다

* ALL_ROWS
** 쿼리 전체 결과를 수행하는 것에 대한 최적화 를 목표로 최저 ㅅ비용의 실행계획을 수립

## 조인 순서 조정을 위한 힌트
* ORDERED
** from 절에 적혀있는 테이블 순서대로 조인 수행

* LEADING
** from 절에 기술할 테이블으 순서와 상관없이 조인 순서를 제어하는 힌트
*** from절의 변경 없이 사용됨
*** ordered힌트와 함께 사용되면 무시

