import threading
threading.stack_size(67108864)


class Edge:

    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Graph:

    def __init__(self, v, e):
        self.vertices = v
        self.edges = e


def read_file(file_path):
    data = utils.read_file(file_path)
    vertices = data[1][0]
    edges = []
    for i in range(1, len(data)):
        edges.append(Edge(data[i][0] - 1, data[i][1] - 1, data[i][2]))
    return Graph(vertices, edges)


def compress(parents):
    for i in range(len(parents)):
        if parents[i][0] != i:
            parents[i] = parents[parents[i][0]]


