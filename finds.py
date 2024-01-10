import csv
import pandas as pd
import numpy as np

data = pd.read_csv("finds.csv",delimiter=",");
print(data);
d = np.array(data);
print(d);
positive = []
for i in range(len(data)):
    if d[i][6].upper() == "YES":
        positive.append(d[i]) 
print(positive);
h = ['%','%','%','%','%','%']
for i in range(6):
      if positive[0][i] != h[i]:
        h[i]=positive[0][i];
print(h);
for x in range(1,3):
    for i in range(6):
        if positive[x][i] != h[i]:
            h[i]="?";
            print(h);
print(h)
