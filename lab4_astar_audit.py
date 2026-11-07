import heapq

graph = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)], "C": [("G", 3)], "G": []}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def astar(graph, h, start, goal, show=False):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    trace = []
    expanded = 0
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best[node]:
            continue
        trace.append(node)
        if show and len(trace) <= 3:
            print("  selected", node, "g =", g, "h =", h[node], "f =", f)
        if node == goal:
            return g, path, trace, expanded
        expanded += 1
        for nxt, w in graph[node]:
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))
        if show and len(trace) <= 3:
            print("  frontier:", sorted([(x[0], x[2]) for x in pq]))

def cost_of(path):
    total = 0
    for i in range(len(path) - 1):
        for n, w in graph[path[i]]:
            if n == path[i + 1]:
                total += w
    return total

print("A* with given h")
g, path, trace, exp = astar(graph, h, "S", "G", True)
print("path:", path, "cost:", g, "summed:", cost_of(path))
print("processed:", trace)
print("expanded:", exp)
print()

zero = {k: 0 for k in h}
print("UCS (h = 0)")
g, path, trace, exp = astar(graph, zero, "S", "G")
print("path:", path, "cost:", g, "summed:", cost_of(path))
print("processed:", trace)
print("expanded:", exp)
print()

h2 = dict(h)
h2["C"] = 10
print("A* with h(C) changed from 2 to 10 (true remaining cost of C is 3)")
g, path, trace, exp = astar(graph, h2, "S", "G")
print("path:", path, "cost:", g, "summed:", cost_of(path))
print("processed:", trace)
print("expanded:", exp)
