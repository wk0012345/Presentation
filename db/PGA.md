# PGA (UGA)영역
## Private Global area
## User Global Area

1. 세션영역
  * 유저가 데이터베이스로 연결할 때 데이터베이스가 유저를 위한 세션을 만든다
  * 유저들의 세션 정보가 저장됨
  * 어떤유저인지 등
  * 디비 이용 끝나면 어플리케이션에서 close를 해 주어야 함
  ex) 자바
   ```con.close()```

2. private sql area

  * persistant area
    각 쿼리가 커서로 바뀌는데, (explicit cursor or implicit cursor.) 이 커서에 사용된 바인딩 정보가 저장되며 릴리즈되면 커서가 닫힌다
    
  * runtime area
    다른 프라이빗 sql 영역은 런타임 영역에 저장된다
  
3. cursor area
  커서의 정보가 저장된다
  
4. sql work area
  디스크에서 리턴된 정보를 조작한다

  * sort area
    - 머지 그룹바이 등등이 이 영역에서 실행되어짐
  * hash join area
  * bitmap merge area
  * bitmap create area
  > 해시조인 비트맵 처리가 PGA에서 처리되어짐
  
# 모든 세션별 운영은 PGA에서 이루어지고 세션별 데이터 작업은 여기에서 이루어진다
 
## 사이즈가 적으면 퍼포먼스가 떨어지고
## 사이즈가 많으면 퍼포먼스가 좋아진다
 
## 오라클은 PGA영역의 사이즈를 자동으로 줄 수 있는데
## 이것은 안쓰는영역은 pga를 줄여주고 많이 쓰는곳은 PGA영역의 크기를 늘릴 수 있기 때문이다
