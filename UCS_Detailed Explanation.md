## ✅ Your UCS Process

When solving UCS manually, you:

1. Start at **S**
2. From **S**, look at all possible neighbors and their **costs**
3. Pick the **least cost path** so far and expand it
4. Always continue expanding the **lowest-cost total path**
5. Stop when you reach the **goal (G)**

This is like Dijkstra’s algorithm — UCS **always expands the path with the smallest cumulative cost so far**.

---

## 🧠 Python UCS Code

Here is the UCS function:

```python
import heapq

def ucs(graph, start, goal):
    visited = set()
    pq = [(0, [start])]  # priority queue of (total_cost, path)

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
```

---

## 🔍 Line-by-Line Explanation

| Line                                            | Meaning                                             |
| ----------------------------------------------- | --------------------------------------------------- |
| `heapq`                                         | Python module to implement a **min-priority queue** |
| `pq = [(0, [start])]`                           | Queue starts with the start node and cost 0         |
| `heapq.heappop(pq)`                             | Always removes the path with **lowest total cost**  |
| `path[-1]`                                      | Last node in the path (current location)            |
| `if node == goal`                               | If the goal is reached, return full path and cost   |
| `if node not in visited:`                       | Avoid revisiting nodes                              |
| `for neighbor, weight in graph[node]:`          | Expand each neighbor and consider cost              |
| `heapq.heappush(pq, (cost + weight, new_path))` | Add new path with updated cost to the queue         |

---

## 🧰 Example: `graph_weighted`

```python
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
```

### First Few Steps Manually:

| Path  | Cost |
| ----- | ---- |
| S → A | 1    |
| S → B | 2    |
| S → C | 3    |

Expand **S → A** (lowest cost), then:

| Path      | Cost |
| --------- | ---- |
| S → B     | 2    |
| S → C     | 3    |
| S → A → D | 5    |

Expand **S → B**, then:

| Path      | Cost |
| --------- | ---- |
| S → C     | 3    |
| S → A → D | 5    |
| S → B → E | 4    |

Expand **S → B → E**, then:

| Path            | Cost |
| --------------- | ---- |
| S → C           | 3    |
| S → A → D       | 5    |
| S → B → E → G ✅ | 5    |

Goal reached with total cost = 5.

---

## 🧩 UCS Guarantees

* **Always finds the path with least cost**, not necessarily the fewest steps.
* The queue **automatically sorts paths** by total cost.
