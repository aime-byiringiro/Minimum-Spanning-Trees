# Krustal Algorithm
- In Krustal's algorithm, set A is a forest whose vertices are all those of the given graph. The safe edge added to A is always the lowest-weight edge in the graph that connects two distinct components. 

- It assumes that the input is connected and represented by adjacency lists. c

# Running time: O(E lg V)

# Pseudocode
 - MST-KRUSKAL(G,w)
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
![Screenshot 2023-12-08 at 2 49 48 PM](https://github.com/aime-byiringiro/Minimum-Spanning-Trees/assets/85495866/703d4863-463a-4e03-952f-a78ecbfa4a8a)


![Screenshot 2023-12-08 at 2 50 04 PM](https://github.com/aime-byiringiro/Minimum-Spanning-Trees/assets/85495866/365c2bfa-ddf4-4b89-bc63-0721d2c09fe5)


