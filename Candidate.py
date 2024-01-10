import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv = pd.read_csv('candidate.csv');
data = np.array(csv.iloc[:,0:-1])
print(data)
target = np.array(csv.iloc[:,-1])
print(target)

 S = ['%'for i in range(len(data[0]))]
print(S)
G = [['?'for i in range(len(data[0]))] for j in range(len(data[0])) ]
print(G)

  S = data[0]
for i in range(len(data)):
    h = data[i]
    if target[i] == "Yes":
        for x in range(len(S)):
            if h[x]!=S[x]:
                S[x]="?";
                G[x][x] = "?";
    if target[i] == "No":
        for x in range(len(S)):
            if h[x]!=S[x]:
                G[x][x] = S[x]
            else:
                G[x][x] = "?"
                
print(S)
print(G[0:2])
        
    
