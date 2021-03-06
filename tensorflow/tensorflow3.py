# Hypothesis using matrix
# https://developers.google.com/machine-learning/crash-course/prereqs-and-prework?hl=ko
'''
https://www.youtube.com/watch?v=fZUV3xjoZSM

최종적으로 우리가 알고 싶은건
어떤 x 값이 들어와도 Y를 알고싶다
W 값을 알고 싶은 것

Y = xw + b
우리는 데이터(x)값도 알고 결과값 (Y)도 알고 있는데
먼저 w를 구하고(코스트 변화량)
어떤 데이터(x) 값이 들어와도 알고있는 w값을 이용하여 결과값 (Y)를 예측 가능하게 한다

최종적으로 우리가 알고싶은건
저 표에없는 새로운 x들이 들어와도
그 결과로 출력되는 Y를 알고싶다는거에요
근데 Y=x1w1+x2w2+x3w3 이렇게 식을 세웠잖아요
그래서 w값들의 매트릭스를 잘 최적화해주면
Y를 알게되는것과 같게되겠죠?

추정과 예측

추정
추정(推定)은 입력된 자료가 불완전하거나 불확실하더라도 사용할 수 있는 계산된 결과의 근삿값이다.
추정 이론과 추정량은 확률분포에 대한 추론과 관련된 주제이다.

예측
예측 분석(predictive analysis)은 데이터 마이닝 기법, 기존 데이터나 미래 상황에 대한 가정을 활용하여 
고객이 제안에 반응을 보이거나 특정 제품을 구매할 확률 등 비즈니스 활동 결과를 예측 하는 것을 말한다.


저기 강의에서 prediction(예측) 이라는 의미로 강의가 전달이 되었다면 저 강의가 잘못된 겁니다.
통계학에서는  estimation(추정) 과 prediction(예측) 은 전혀 다른 이야기에요.
선형회귀분석에서는 모델 가정이

	(*)E(Y) = W’X + e
	e ~ N(0, I * sigma), N 은 정규분포

이에요. 그리고 X 는 통계 변수가 아니라 수학변수라서 상수취급됩니다.
그러면 이제 추정(estimation)에 대해서 설명을 드릴 건데 추정이 무엇이냐면, 

Example) N(3, 2/3) 분포, 즉 평균이 3이고 분산이 2/3인 분포에서 데이터가 {3, 2, 3, 4} 로 주어졌다면
평균공식이라는 함수 mu(X) = mu({3, 2, 3, 4}) = 1/4 * (3 + 2 + 3 + 4) = 3 이고
표본분산공식이라는 함수 s(X) = s({3, 2, 3, 4}) = 1/(4 - 1) * (0 + 1 + 0 + 1) = 2/3 이므로

평균공식에 따라서 나온 값이 모평균과 정확히 “일치”하고
표본분산공식에 따라서 나온 값이 모분산과 정확히 “일치”하므로
우리는 이 “공식”들을 “불편”, 즉 “일치하지 않음이 없다”고 정의를 해요.

그리고 회귀분석은 데이터 X 의 분포에 따른 Y 의 분포를 추정함에 있어
(*)에서 정의됨과 같이 좌변과 우변이 일치하겠끔 W, 즉 가중치를 조절함으로 “불편추정량”을 구하는 것입니다.

예측은 이제 여기서 구해진 가중치로 미래에 들어오는 X 값들로부터 Y 값을 예측을 하는 것인데
이 예측값이 예측값이 어느 구간안에 있을 확률, 즉 “구간 추정”에 따른 confidence interval 을 구해서 실제로 있을만한 값인지 아닌지를 보는 것입니다.
'''

'''
리니어 리그레션

선형회귀
	선형 적인 회귀
	
	회귀 연속적인 모델의 값 예측(Hypothesis)

	즉 선형적인 연속적의 모델의 값 예측

y = ax + b

x = 데이터
y = 결과값
b = 절편

코스트 우리가 세운 가설(Hypothesis)과 실제 데이터 값이 얼마나 차이가 나는지에 대한 값


코스트는 가설- 실제값의 차이를 제곱한 값을 모두 더하여 데이터의 갯수만큼 나눔

코스트 함수를 보면 2차함수가 나오는데 기울기가 가장 적은 곳을 찾아냄

경사 하강법 그레디언트 디센트를 이용

어떤 점을 잡더라도 경사를 보아서 옆쪽으로 계속 이동함

리니어 리그레션


학습을 한다는것은 우리가 가장 적은 코스트를 찾아 낸다는것



'''


import tensorflow as tf
# Matrix 
xData =[[73.,80.,75.],
        [93.,88.,93.],
		[89.,91.,90.],
		[96.,98.,100.],
		[73.,66.,70.]]
yData =[[152.],
		[185.],
		[180.],
		[196.],
		[142.]]

X = tf.placeholder(tf.float32,shape=[None,3])
Y = tf.placeholder(tf.float32,shape=[None,1])

W = tf.Variable(tf.random_normal([3,1], name='weight'))
b = tf.Variable(tf.random_normal([1]), name='bias')

#hypothesis (선형회귀의 예측 선 (가설))
hypothesis = tf.matmul(X,W) + b

#Simplified cost/loss function (코스트 함수)
cost = tf.reduce_mean(tf.square(hypothesis-Y))

#Minimize (선형회귀를 추정값을 구하기 위하여 씀)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)

#cost를 최소화 하는 작업
train = optimizer.minimize(cost)

# session 초기화
sess = tf.Session()

# 변수 초기화
sess.run(tf.global_variables_initializer())

for step in range(5001):
	cost_val , hy_val , _ = sess.run([cost,hypothesis,train],feed_dict={X:xData,Y:yData})

	if step % 50 == 0:
		print(step,"cost : " , cost_val , "\n Prediction: \n",hy_val)