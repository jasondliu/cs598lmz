import sys, threading
threading.Thread(target=lambda: input('Press enter to exit')).start()
 
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.distance = sys.maxsize
        self.color = 'black'
 
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
 
class Graph:
    vertices = {}
 
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
 
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
               
