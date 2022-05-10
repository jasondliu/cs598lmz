import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

# load the graph from the file and set up the nodes and edges
G = nx.read_gpickle("data/dblp-coauthors.gpickle")
nodes = G.nodes()
edges = G.edges()

# define the plot
plt.figure(figsize=(20,20))

# plot the nodes
nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color='r', node_size=50, alpha=0.8)

# plot the edges
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1.0, alpha=0.5)

# show the plot
plt.show()

# save the plot
plt.savefig("data/dblp-coauthors.png")
