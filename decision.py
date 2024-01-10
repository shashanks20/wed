import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("decision.csv")
print(data)
x = data.iloc[:,0:-1]
y = data.iloc[:,-1]
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
h = LabelEncoder()
x.Outlook = h.fit_transform(x.Outlook)
x.Temperature = h.fit_transform(x.Temperature)
x.Humidity = h.fit_transform(x.Humidity)
x.Windy = h.fit_transform(x.Windy)

y = h.fit_transform(y)

print(x)
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5,random_state=42)
from sklearn.tree import DecisionTreeClassifier,export_text,plot_tree
md = DecisionTreeClassifier()
md.fit(x_train,y_train) 

plot_tree(md,feature_names=list(x.columns),rounded=True)
plt.show()
from sklearn.metrics import accuracy_score
y_pred = md.predict(x_test)
accuracy = accuracy_score(y_pred, y_test,normalize=True)
print(f"Accuracy: {accuracy}")


