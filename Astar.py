def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist[n]

def aStarAlgo(graph,start,stop):
    opens = set(start);
    closed = set();
    g={start:0};
    parent={start:start};
    while open:
        n = min(opens,key=lambda node : g[node]+heuristic(node));
        
        if n==stop or not graph[n]:
            break
        opens.remove(n);
        
        for m,w in graph[n].items():
            if m not in closed and m not in opens:
                opens.add(m)
                parent[m],g[m]=n,g[n]+w
            if g[m]>g[n]+w:
                parent[m],g[m]=n,g[n]+w
                if(m in closed):
                    opens.add(m)
                    closed.remove(m)
        closed.add(n)
    path=[n]
    while parent[n]!= n :
        x = parent[n]
        path.append(x)
        n = parent[n]
    path.reverse()
    print(path)
graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'A': 2, 'C': 1, 'G': 9},
    'C': {'B': 1},
    'D': {'E': 6, 'G': 1},
    'E': {'A': 3, 'D': 6},
    'G': {'B': 9, 'D': 1}
}
aStarAlgo(graph,'A', 'G')
