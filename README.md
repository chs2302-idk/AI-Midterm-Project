| Name | NRP | Kelas |
| --- | --- | --- |
| Ahmad Farras Favian Al Efasi | 5025251005 | IUP |
| Rozan Hakim Abyandhono | 5025251257 | IUP |
| Aqeela Chessa Nurcahyo | 5025251163 | IUP |
| Valian Athalla Syahputra | 5025251156 | IUP |

# Group 6 - Route Planning on Java Domestic Flight Network Using Uninformed Search Algorithms
**Algorithm Name**

```
Paste Here
```

**Algorithm Name**

```
Paste Here
```

**DFS (Depth-First Search)**

```
import time

GRAPH = {
    'CGK': {'BDO': 250, 'SRG': 500, 'SUB': 1000, 'YIA': 550},
    'BDO': {'CGK': 250, 'YIA': 300},
    'SRG': {'CGK': 500, 'SUB': 400},
    'SUB': {'CGK': 1000, 'SRG': 400, 'BWX': 700, 'MLG': 200, 'YIA': 450},
    'YIA': {'CGK': 550, 'BDO': 300, 'SUB': 450, 'MLG': 600},
    'MLG': {'SUB': 200, 'YIA': 600, 'BWX': 300},
    'BWX': {'SUB': 700, 'MLG': 300},
}


def dfs(start, goal):
    """Depth-First Search using a LIFO stack and a visited set.
    Neighbors are explored in alphabetical order."""
    stack = [[start]]          
    visited = set()
    expanded = []              

    while stack:
        path = stack.pop()     
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        expanded.append(node)

        if node == goal:
            return path, expanded

        for neighbor in reversed(sorted(GRAPH[node])):
            if neighbor not in visited:
                stack.append(path + [neighbor])
    return None, expanded


def route_cost(path):
    return sum(GRAPH[a][b] for a, b in zip(path, path[1:]))


if __name__ == "__main__":
    start_time = time.perf_counter()
    path, expanded = dfs('CGK', 'BWX')
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    print("Route          :", " -> ".join(path))
    print("Flights        :", len(path) - 1)
    print("Total cost     : Rp{:,}".format(route_cost(path) * 1000))
    print("Nodes expanded :", len(expanded), expanded)
    print("Running time   : {:.4f} ms".format(elapsed_ms))

```
