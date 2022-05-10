fn = lambda: None
# Test fn.__code__.co_name for python 2.7 and 3
get_fn_name = getattr(fn, '__func__').__code__.co_name


def _tree_to_graph(tree):
    graph = networkx.DiGraph()
    stack = []
    stack.append((tree, None))
    while stack:
        node, parent = stack.pop(0)
        if not (isinstance(node, nltk.Tree)):
            continue
        if parent is None:
            graph.add_node(node.node, parent=None)
            u = node.node
        else:
            graph.add_node(node.node, parent=parent.node)
            u = node.node
            v = parent.node
            graph.add_edge(u, v, label=node.label())
        for child in node:
            stack.append((child, node))
    return graph

def nltk2networkx(tree):
    '''Take a nltk Tree and return a networkx MultiDiGraph
    '''
    graph = _tree_
