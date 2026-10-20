| Name | NRP | Kelas |
| --- | --- | --- |
| Ahmad Farras Favian Al Efasi | 5025251005 | IUP |
| Rozan Hakim Abyandhono | 5025251257 | IUP |
| Aqeela Chessa Nurcahyo | 5025251163 | IUP |
| Valian Athalla Syahputra | 5025251156 | IUP |

# Group 6 - Route Planning on Java Domestic Flight Network Using Uninformed Search Algorithms

**Problem Introduction**

Indonesia relies on air transportation to connect cities across its many islands. However, not every pair of cities has a direct flight, so passengers may need to transfer through other airports. Different routes can also have different ticket prices and numbers of flights, making it difficult to determine the most suitable route manually.

This project models a domestic flight network from CGK (Soekarno-Hatta International Airport) to BWX (Banyuwangi Airport) as a weighted graph, where airports represent nodes, flight connections represent edges, and ticket prices represent edge weights.

The project implements and compares three uninformed search algorithms: Breadth-First Search (BFS), Uniform-Cost Search (UCS), and Depth-First Search (DFS). The algorithms are evaluated based on the routes they find, total ticket costs, number of flights, expanded nodes, and execution time to understand the differences between their search strategies.

**Uniform Cost Search (UCS)**

"""Uniform Cost Search: cheapest flight route from Jakarta (CGK) to Banyuwangi (BWX).
Prices are in thousand Rupiah. All flights run in both directions."""
import heapq

FLIGHTS = [
    ("CGK", "BDO", 250), ("CGK", "SRG", 500), ("CGK", "YIA", 550), ("CGK", "SUB", 1000),
    ("BDO", "YIA", 300), ("SRG", "SUB", 400), ("YIA", "SUB", 450), ("YIA", "MLG", 600),
    ("SUB", "MLG", 200), ("SUB", "BWX", 700), ("MLG", "BWX", 300),
]

def build_graph(flights):
    graph = {}
    for a, b, price in flights:
        graph.setdefault(a, []).append((b, price))
        graph.setdefault(b, []).append((a, price))
    return graph

def ucs(graph, start, goal, verbose=True):
    frontier = [(0, start)]          
    best_g = {start: 0}            
    parent = {start: None}           
    explored = set()
    expanded = []

    while frontier:
        g, node = heapq.heappop(frontier)
        if node in explored or g > best_g[node]:
            continue                
        if verbose:
            print(f"Pop {node} (g={g})")
        if node == goal:             
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], g, expanded

        explored.add(node)
        expanded.append(node)
        for nxt, price in graph[node]:
            new_g = g + price
            if nxt not in explored and new_g < best_g.get(nxt, float("inf")):
                best_g[nxt] = new_g
                parent[nxt] = node
                heapq.heappush(frontier, (new_g, nxt))
        if verbose:
            waiting = sorted((best_g[n], n) for n in best_g if n not in explored)
            print("   frontier:", ", ".join(f"{n} {c}" for c, n in waiting) or "empty")
    return None, float("inf"), expanded

if __name__ == "__main__":
    graph = build_graph(FLIGHTS)
    path, cost, expanded = ucs(graph, "CGK", "BWX")
    print("\nPath:", " -> ".join(path))
    print("Flights:", len(path) - 1)
    print("Total price:", cost, "(thousand Rp)")
    print("Expanded order:", ", ".join(expanded))


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
