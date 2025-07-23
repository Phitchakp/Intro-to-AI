graph_unweighted = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]           # Stack of paths

    while stack:
        path = stack.pop()      # Get last path
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None

print("DFS path:", dfs(graph_unweighted, 'A', 'G'))