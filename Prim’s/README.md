# Prim Algorithm 
- In Prim's algorithm, set A always forms a single tree. A tree starts from an arbitrary root vertex r and grows until it spans all the vertices in the V graph. 

- It assumes that the input is a connected represented by an adjacency list.


# Pseudocode
ter- MIST-PRIMT(G,W,r)
1.      for each vertex u ∈ G.V
2.          u.key = ∞
3.          u.∏ = NIL
4.      r.key = 0
5.      Q = ⦰ 
6.      for each vertex u ∈  G.V
7.          INSERT (Q,u)
8.      while Q ≉ ⦰
9.          u = EXTRACT-MIN(Q) // add u to the tree
10.         for each vertex v in G.Adj[u] // update u's non-tree neighbors 
11.             if v ∈  Q and w(u,v) < v.key
12.                 v.∏ = u
13.                 v.key = w(u,v)
14.                 DECREASE-KEY(Q,v,w(u,v))


# Image

![Screenshot 2023-12-08 at 3 53 31 PM](https://github.com/aime-byiringiro/Minimum-Spanning-Trees/assets/85495866/d6313455-cd6a-439b-ba40-e26d7dc565e3)

