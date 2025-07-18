## ✅ Manual DFS Approach

When doing **DFS manually**, you likely:

1. Start at node **A**
2. Explore **B** (first child of A)
3. From **B**, go to **E** (first child of B)
4. Since E has no children, backtrack to B, then go to **F**
5. Backtrack to A, go to **C**, etc.
6. Eventually reach **G**

This is a **depth-first traversal**, where you **go deep down a path** until there's nothing left, then **backtrack**.

---

## 🧠 Python DFS Code

Here’s the DFS implementation:

```python
def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]  # Stack stores paths (list of nodes)

    while stack:
        path = stack.pop()       # Get the latest path added (LIFO)
        node = path[-1]          # Look at the last node in that path

        if node == goal:
            return path          # Return the path if goal found

        if node not in visited:
            visited.add(node)   # Mark the node as visited
            for neighbor in reversed(graph[node]):  # Explore children
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)  # Push new extended path
```

---

## 🔍 How It Matches Your Manual Process

| Manual Step                   | Code Equivalent                                                              |
| ----------------------------- | ---------------------------------------------------------------------------- |
| Start at A                    | `stack = [[start]]` creates path `['A']`                                     |
| Visit A                       | `path = stack.pop()` gives `['A']`, `node = 'A'`                             |
| Go to B                       | `for neighbor in reversed(graph['A'])` includes B (first)                    |
| Go to E                       | Continue extending the path to `['A', 'B', 'E']`                             |
| E has no children → backtrack | No new nodes added → pop next path                                           |
| Visit F                       | `['A', 'B', 'F']` gets added and explored                                    |
| Eventually go to D → G        | D is added as `['A', 'D']`, then `['A', 'D', 'G']` is added and matches goal |

---

## 🧰 Key Concepts

### 🔁 Stack (DFS uses LIFO)

```python
stack = [[start]]
...
path = stack.pop()
```

This ensures the **last path added** is the first explored — meaning **deeper paths get explored first**.

---

### 🔃 Path Tracing

Instead of storing only nodes, we store **entire paths** in the stack:

```python
new_path = list(path)
new_path.append(neighbor)
stack.append(new_path)
```

This helps us **return the full path** when we reach the goal.
