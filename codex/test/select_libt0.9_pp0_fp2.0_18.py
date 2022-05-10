import selection_mods as smods
from IPython.display import display
import networkx as nx
G = nx.read_graph6("graphs/g415.txt")
G = nx.convert_node_labels_to_integers(G)

degrees = [G.degree[i] for i in G]
order = sorted(range(0, len(degrees)), key=lambda x: degrees[x], reverse=True)
gx = nx.convert_node_labels_to_integers(G,order=order)
gx.edges()

nx.draw(gx, node_color='y')

import numpy as np

def reduced(mindegree,verts,xverts):
    n = len(verts)
    nxverts = [i for i in range(0,n) if i not in xverts]
    nxverts.append(-1)
    rgraph = Graph(nx.Graph(nx.induced_subgraph(G, nxverts)))
