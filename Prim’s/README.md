# Prim Algorithm 
- In Prim's algorithm, set A always form a single tree. A tree starts from an arbitrary root vertex r and grows until it spans all the vertices in V graph. 

- It assumes that the input is a connected represented by adjaceny list.


# Pseudocode
ter- MIST-PRIMT(G,W,r)
1.      for each vertext u ∈ G.V
2.       u.∏ = NIL
3.      r.key = 0
4. Q = ⦰ 
5. for each vertex u ∈  G.V
6.  INSERT (Q,u)
7. while Q ≉ ⦰
8.  u = EXTRACT-MIN(Q) // add u to the tree
9.  for each vertex v in G.Adj[u] // update u's non-tree neighbors 
10.     if v ∈  Q and w(u,v) < v.key
11.         v.∏ = u
12.         v.key = w(u,v)
13.         DECREASE-KEY(Q,v,w(u,v))


# Image