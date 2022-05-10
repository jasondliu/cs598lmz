import gc, weakref, pprint

class Graph(object):
    """
    A directed graph implemented using a weak reference map to its nodes.
    
    ----------------
    Nodes are instances of the Node class, defined below.
    
    Because of the use of weak references, the Graph object just tends
    to grow and shrink whenever nodes are added or deleted.
    
    A common way to use this is:
    
        G = Graph()
        G.root = Graph.Node(G)
        G.wombat = Graph.Node(G)
        G.root.connect(G.wombat)
    
    -------------------------------------
    To produce an image of the graph in dot:
    
        G = Graph()
        G.root = Graph.Node(G)
        G.cheese = Graph.Node(G)
        G.dill = Graph.Node(G)
        G.root.connect(G.cheese)
        G.cheese.connect(G.dill)
        print G.to_dot()
    
    This produces dot content that looks like this:
    
        digraph g
