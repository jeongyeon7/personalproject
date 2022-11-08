import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("height.csv")
print(df.head(10))

#산점도 출력
X = df["height"] #독립변수 키 (독립변수는 주로 대문자 사용)
y = df["weight"] #종속변수 몸무게

plt.plot(X,y,'o')
plt.show()

print(X[:10])
print("=" * 30)
print(y[:10])
print("=" * 30)

#훈련용 데이터 생성
XData = X.values.reshape(-1,1)
print(XData[:10])
print("=" * 30)

#test용 데이터 자르기
X_train, X_test, y_train, y_test = train_test_split(XData,y,random_state=42)

#선형회귀 분류기 생성
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#분류기에 학습(training) 시키기
lr.fit(X_train,y_train)

#학습 결과 출력
plt.plot(X,y,"o")
plt.plot(X,lr.predict(XData))
plt.show()

#기울기
print(lr.coef_)
print("=" * 30)
#절편
print(lr.intercept_)
print("=" * 30)

#키 70인치의 몸무게 예측
print(lr.predict([[70]]))

#Ridge회귀를 이용한 성능 확인하기
from sklearn.linear_model import Ridge

ridge = Ridge()

#훈련
ridge.fit(X_train,y_train)

#학습결과
plt.plot(X,y,"o")
plt.plot(X,ridge.predict(XData))
plt.show()

#기울기
print(ridge.coef_)
print("=" * 30)
#절편
print(ridge.intercept_)
print("=" * 30)

#키 70인치의 몸무게 예측 ridge모델
print(ridge.predict([[70]]))

"""
Ridge회귀 alpha값에 따른 일반화 확인하기
aplha값을 높이면 계수를 0에 더 가깝게 만들어
훈련세트의 성능은 나빠지지만 일반화는 쉬워진다
"""
ridge10 = Ridge(alpha=10) #alpha값을 찾아내는게 관건

#훈련
ridge10.fit(X_train,y_train)
#학습 결과
plt.plot(X,y,"o")
plt.plot(X,ridge10.predict(XData))
plt.show()

#기울기
print(ridge10.coef_)
print("=" * 30)
#절편
print(ridge10.intercept_)
print("=" * 30)

#키 70인치의 몸무게 예측 ridge모델
print(ridge10.predict([[70]]))

#알파값을 0.1로 변경 후 훈련
ridge01 = Ridge(alpha=0.1) #alpha값을 찾아내는게 관건

#훈련
ridge01.fit(X_train,y_train)
#학습 결과
plt.plot(X,y,"o")
plt.plot(X,ridge01.predict(XData))
plt.show()

#기울기
print(ridge01.coef_)
print("=" * 30)
#절편
print(ridge01.intercept_)
print("=" * 30)

#키 70인치의 몸무게 예측 ridge모델
print(ridge01.predict([[70]]))
