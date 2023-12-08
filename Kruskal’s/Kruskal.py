# Finding the minimum spanning tree of an undirected weighteed graph using Krustal's algorithm
# Some of these codes were developed in reference to geeksforgeeks


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.G = []

        # Adding an edge to a graph

    def addEdge(self, u, v, w):
        self.G.append([u, v, w])

    # Finding the parent of a a vertex at i
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    """
    End of Graph creation 
    """

    """
    Kruskal's algo 
    """

    def Krustal_algorithm(self):
        result = []  # contain the results from spanning
        i = 0
        e = 0
        # sort all the edges according to thier weights in a non-decreasing order.
        # This is a condition for all greedy algorithms
        self.graph = sorted(self.G, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.G[i]

            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Edges in teh constructed MST")
        for u, v, weight in result:
            minimum_cost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimu Spanning Tree", minimum_cost)


if __name__ == "__main__":
    g = Graph(4)

    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.Krustal_algorithm()
