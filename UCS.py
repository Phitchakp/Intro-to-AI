import heapq            # Priority Queue implementation

graph_weighted = {
    'S': [('A', 1), ('B', 2), ('C', 3)],
    'A': [('D', 4)],
    'B': [('E', 2)],
    'C': [('F', 5)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'F': [('G', 6)],
    'G': []
}

def ucs(graph, start, goal):
    visited = set()
    pq = [(0, [start])]                 # Priority queue stores (cost, path)

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (cost + weight, new_path))

    return None, float('inf')

path, cost = ucs(graph_weighted, 'S', 'G')
print("UCS path:", path, "with cost:", cost)