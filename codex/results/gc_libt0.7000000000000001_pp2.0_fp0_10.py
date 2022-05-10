import gc, weakref
from collections import Counter


G = nx.Graph()

G.add_edge(1, 2, color="red")
G.add_edge(2, 3, color="blue")
G.add_edge(3, 4, color="green")
G.add_edge(4, 1, color="black")
G.add_edge(1, 3, color="red")
G.add_edge(2, 4, color="blue")

print(nx.shortest_path(G, 1, 4, weight="weight"))

print(nx.shortest_path(G.to_directed(), 1, 4, weight="weight"))

print(list(nx.all_simple_paths(G, 1, 4)))

print(G.number_of_edges())

print(G.number_of_nodes())

print(G.size())

print(G.nodes(data=True))

print(G.edges(data=True))


print(G.degree())

print(G.degree(weight="weight"))
