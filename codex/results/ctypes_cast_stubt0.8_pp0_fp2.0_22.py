import ctypes
ctypes.cast(ctypes.py_object(g), ctypes.c_void_p).value

cm = matplotlib.cm.get_cmap('RdYlBu')
norm = matplotlib.colors.Normalize(vmin=0, vmax=g.number_of_nodes())
nx.draw(g, pos=nx.spring_layout(g), node_color=cm(norm(g.nodes())), cmap=cm, with_labels=True)
plt.show()
 
</code>

