import gc, weakref

class Edge(object):
    """A directed edge between two nodes of a graph."""
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.src.out.add(self)
        self.dst.in_.add(self)

    def delete(self):
        self.src.out.remove(self)
        self.dst.in_.remove(self)
        self.src = None
        self.dst = None

class Node(object):
    """A node in a graph. The graph is represented by an adjacency list."""
    def __init__(self):
        self.out = set()
        self.in_ = set()
    def delete(self):
        while self.out:
            self.out.pop().delete()
        while self.in_:
            self.in_.pop().delete()

def test_graph():
    n = Node()
    n.out.add(Edge(n, n))
    n.delete()
    print gc
