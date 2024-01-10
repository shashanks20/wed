import pandas as pd

data = pd.read_csv("naive.csv");

print(data)

from sklearn.preprocessing import LabelEncoder

x = data.iloc[:,0:-1]
y = data.iloc[:,-1]
hi = LabelEncoder()
x.Outlook = hi.fit_transform(x.Outlook)
x.Temperature = hi.fit_transform(x.Temperature)
x.Humidity = hi.fit_transform(x.Humidity)
x.Windy = hi.fit_transform(x.Windy)
print(x)

y = hi.fit_transform(y)

print(y)

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
md = GaussianNB()
md.fit(x_train,y_train)
y_pred = md.predict(x_test)
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_pred,y_test)
print(acc)
