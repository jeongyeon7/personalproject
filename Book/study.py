import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

#파일 불러오기
df = pd.read_csv("height.csv")
print(df.head(10))

#산점도 출력
X = df["height"] #독립변수 키 
y = df["weight"] #종속변수 무게

plt.plot(X,y,"o")
plt.show()

#훈련용 (학습용)데이터 생성
Xdata = X.values.reshape(-1,1)
print(Xdata)