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
    frontier = [(0, start)]            # priority queue of (g, airport)
    best_g = {start: 0}                # cheapest known cost to each airport
    parent = {start: None}             # used to rebuild the path
    explored = set()
    expanded = []

    while frontier:
        g, node = heapq.heappop(frontier)
        if node in explored or g > best_g[node]:
            continue                   # stale entry, a cheaper one was already handled

        if verbose:
            print(f"Pop {node} (g={g})")
        if node == goal:               # goal test when popped, not when generated
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
