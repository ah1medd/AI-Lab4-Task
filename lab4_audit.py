import heapq

graph = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)], "C": [("G", 3)], "G": []}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def true_cost(node):
    if node == "G":
        return 0
    best = float("inf")
    for nxt, w in graph[node]:
        best = min(best, w + true_cost(nxt))
    return best

def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded = 0
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            continue
        if node == goal:
            return g, path, expanded
        expanded += 1
        for nxt, w in graph[node]:
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))

def audit(h):
    print("node | true remaining | h | admissible")
    for n in h:
        t = true_cost(n)
        print(n, "|", t, "|", h[n], "|", h[n] <= t)
    print("edge | h(u) | cost + h(v) | consistent")
    for u in graph:
        for v, w in graph[u]:
            print(u + "->" + v, "|", h[u], "|", w + h[v], "|", h[u] <= w + h[v])

print("audit of the given heuristic")
audit(h)
print()
h2 = dict(h)
h2["C"] = 10
print("audit with h(C) = 10")
audit(h2)
print()
print("one overestimate at a time (true remaining cost + 7)")
for n in ["S", "A", "B", "C"]:
    hh = dict(h)
    hh[n] = true_cost(n) + 7
    g, path, exp = astar(graph, hh, "S", "G")
    print("h(" + n + ") =", hh[n], "->", path, "cost", g, "expanded", exp)
