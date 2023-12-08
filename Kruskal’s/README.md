# Krustal Algorithm
- In Krustal's algorithm, set A is a forest whose vertices are all those of the given graph. The safe edge added to A is always the lowest-weight edge in the graph that connects two distinct components. 

- It assumes that the input is connected and represented by adjacency lists. c

# Pseudocode
 -      MST-KRUSKAL(G,w)
 1.     A = ∅ 
 2.     for each Evertex v ∊ G.V
 3.       MAKE-SET(v)
 4.     create a single list of the edges in G.E
 5.     for the list of edges in monotonically increasing order by weight w
 6.     for each edge (u,v) taken from the sorted list in order 
 7.     if FIND-SET(u)≉ FIND-SET(v)
 8.         A = A ∪ {(u,v)}
 9.         UNION(u,v)
 10.     return A


