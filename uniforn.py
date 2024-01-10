def UCS(graph,start,goal):
    li = []
    visited=set(start)
    heapq.heappush(li,(0,start,[start]));
    while li :
        cost,n,path = heapq.heappop(li);
        if n==goal:
            return cost,path;
        for m,w in graph[n].items():
            if m not in visited:
                heapq.heappush(li,(cost+w,m,path+[m]))
                visited.add(m);
    return None

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 2, 'E': 3},
    'C': {'D': 1, 'F': 5},
    'D': {'G': 1},
    'E': {'G': 2},
    'F': {},
    'G': {}
}

start = 'A'
goal = 'F'

total_cost, path = UCS(graph, start, goal)

print("Path:", path)
print("Total cost:", total_cost)
