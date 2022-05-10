import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

class Vertex:
    def __init__(self, name):
        self.name = str(name)

        self.discovery = -1
        self.low = float('inf')
        self.parent = None

        self.children = set()
        self.is_articulation = False
        self.is_bridge = False

        self.visited = False


class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]
        self.vertices = [None] * size

    def add_edge(self, frm, to):
        self.graph[frm - 1].append(to - 1)
        self.graph[to - 1].append(frm - 1)

    def create_vertices(self):
        for i in range(self.size):
            self.vertices[i] = Vertex(i + 1)

