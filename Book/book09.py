import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = sns.load_dataset("iris")
print(iris)
print("=" * 30)

#그래프 표시
sns.set(style="ticks", color_codes=True)
g = sns.pairplot(iris, hue="species",palette="husl")

#부꽃 데이터 세트를 로딩합니다
iris = load_iris()

"""
iris.data는 iris데이터 세트에서 피처만으로 된 데이터를 numpy로 가지고 있는다
"""
iris_data = iris.data
print(iris_data[:10])

#iris.target은 붓꽃 데이터세트에서 레이블 데이터를 numpy로 가지고 있다
iris_label = iris.target
print("iris target 값 : ",list(set(iris_label)))
print("iris target 명 : ",iris.target_names)

"""
붓꽃 데이터 세트를 자세히 보기 위해 dataframe으로 변환한다
"""
iris_df = pd.DataFrame(data=iris_data,columns=iris.feature_names)
iris_df["label"] = iris.target
print(iris_df.head(10))

X_train, X_test, y_train, y_test = train_test_split(iris_data,iris_label,test_size=0.2,random_state=11)

#KNN을 이용한 품종 분류
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=2) #이웃을 늘려가면서 정확도를 1에가깝게 돌림

#KNN분류기를 훈련셋으로 훈련시킴
knn.fit(X_train,y_train)

#테스트셋의 라벨값을 예측한다
y_pred = knn.predict(X_test)

#예측 정확도는 1에 가까울수록 완벽한 것
print("예측 정확도 : {0:.4f}".format(np.mean(y_pred == y_test)))
print("=" * 30)

#새로운 품종 예측
X_new = np.array([[5, 2.9, 1, 0.2]])
prdct = knn.predict(X_new)
print("예측값 : {}, ".format(prdct), "예측한 품종 : {}".format(iris["target_names"][prdct]))
print("=" * 30)

#decision tree를 이용한 품종 분류---------------------------------------
from sklearn.neighbors import DecisionTreeClassifier

#DecisionTreeClassifier객체 생성
dt_clf = DecisionTreeClassifier(random_state=11)

#학습 수행
dt_clf.fit(X_train, y_train)

#학습이 완료된 DecisionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행
pred = dt_clf.predict(X_test)

#정확도 측정
from sklearn.metrics import accuracy_score
print("예측정확도 : {0:.4f}".format(accuracy_score(y_test,pred)))
print("=" * 30)
