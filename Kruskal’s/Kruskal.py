class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal_algorithm(self):
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        result = []

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1

        self.graph = sorted(self.graph, key=lambda item: item[2])

        for edge in self.graph:
            u, v, w = edge
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                result.append((u, v, w))
                union(root_u, root_v)

        return result


# Example usage
g = Kruskal(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

result = g.kruskal_algorithm()
print(result)
