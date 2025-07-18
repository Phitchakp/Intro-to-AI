graph_unweighted = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

from collections import deque

def bfs(graph, start, goal):
    visited = set()             # To avoid visiting the same node twice
    queue = deque([[start]])    # Queue stores paths, not just nodes

    while queue:
        path = queue.popleft()  # Get first path in queue
        node = path[-1]         # Look at last node in the path

        if node == goal:
            return path         # Goal found

        if node not in visited:
            visited.add(node)               # Mark as visited
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)      # Add new path to the queue

    return None                 # No path found

print("BFS path:", bfs(graph_unweighted, 'A', 'G'))