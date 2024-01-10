from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
dt = load_iris()
x = dt["data"]
y = dt["target"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1)
md = KNeighborsClassifier()
md.fit(x_train,y_train)
y_pred = md.predict(x_test)
acc = accuracy_score(y_pred,y_test)
print(acc)
