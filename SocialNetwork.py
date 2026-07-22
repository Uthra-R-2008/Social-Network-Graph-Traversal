graph ={
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A","F"],
    "D":["B"],
    "E":["B","F"],
    "F":["C","E"]
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node,end=" ")
        
        for neighbour in graph[node]:
            dfs(neighbour)
            
print("DFS Traversal: ")
dfs("A")

visited = []
queue = []
print("\n\nBFS Traversal")

visited.append("A")
queue.append("A")

while queue:
    
    node=queue.pop(0)
    print(node,end=" ")
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)