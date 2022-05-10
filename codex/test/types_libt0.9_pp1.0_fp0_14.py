import types
types.xrange = xrange

from dijkstar import Graph, find_path

GRAPH_FILE = "../problems/tsplib/ulysses16.tsp"

class TSPGraph:
    def __init__(self, file_name):
        self.graph = Graph()

        with open(file_name) as f:
            data = f.readlines()

        coordinates = []
        for line in data:
            if line[:7] == "NODE_CO":
                coordinates = [line.split()[1:3] for line in data
                               if line[0] != " " and  line[0] != "E"][5:]

        for u in xrange(len(coordinates)):
            for v in xrange(len(coordinates)):
                if u != v:
                    u_coord = (int(coordinates[u][0]), int(coordinates[u][1]))
                    v_coord = (int(coordinates[v][0]), int(coordinates[v][1]))
                    self.graph.add_
