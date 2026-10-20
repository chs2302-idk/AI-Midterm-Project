
from collections import deque
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


def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}
    expanded = []

    while queue:
        path = queue.popleft()
        node = path[-1]
        expanded.append(node)

        if node == goal:
            return path, expanded

        for neighbor in sorted(GRAPH[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None, expanded


def route_cost(path):
    return sum(GRAPH[a][b] for a, b in zip(path, path[1:]))


if __name__ == "__main__":
    start_time = time.perf_counter()
    path, expanded = bfs('CGK', 'BWX')
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    if path:
        print("Route          :", " -> ".join(path))
        print("Flights        :", len(path) - 1)
        print("Total cost     : Rp{:,}".format(route_cost(path) * 1000))
        print("Nodes expanded :", len(expanded), expanded)
        print("Running time   : {:.4f} ms".format(elapsed_ms))
    else:
        print("No route found.")
