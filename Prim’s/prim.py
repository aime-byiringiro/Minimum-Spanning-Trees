import heapq

def prim(graph):
    n = len(graph)
    key = [float('inf')] * n
    parent = [None] * n
    pq = [(0, 0)]  # Initial vertex with key 0

    while pq:
        current_key, u = heapq.heappop(pq)

        for v, weight in graph[u]:
            if weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))

    return parent

# Example usage
graph = {
    0: [(1, 2), (2, 1)],
    1: [(0, 2), (2, 3)],
    2: [(0, 1), (1, 3)],
    3: [(1, 3), (2, 4)]
}

result = prim(graph)
print(result)
