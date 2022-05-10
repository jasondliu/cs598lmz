import gc, weakref, operator

class Graph(dict):
    """Graph class with self-loops, parallel edges (all of equal weight), and
    the ability to remove them via overloaded operators.

    """
    def __init__(self, iterable):
        self.edge_factory = self
        super(Graph, self).__init__(iterable)

    def __repr__(self):
        if len(self) > 15:
            return '<%s with %d nodes>' % (self.__class__.__name__, len(self))
        else:
            return '<%s %r>' % (self.__class__.__name__, dict(self))

    def __str__(self):
        """Return a string representation of `self`."""
        return repr(self)

    def get_node(self, n):
        """Get node object for node `n`."""
        try:
            return self[n]
        except KeyError:
            raise NetworkXError, 'node %s not in graph' % (n,)

    def adj_list
