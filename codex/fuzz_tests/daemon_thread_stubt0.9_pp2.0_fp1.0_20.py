import sys, threading

def run():
    line = sys.stdin.readline().rstrip()
    while line != "":
        tokens = line.split(' ')
        cmd = tokens[0]
        #print 'cmd ='+cmd
        try:
            if cmd == 'is_adj':
                v1 = int(tokens[1])
                v2 = int(tokens[2])
                print 'is_adj='+str(graph.is_adj(v1, v2))
            elif cmd == 'num_vertices':
                print 'num_vertices='+str(graph.num_vertices())
            elif cmd == 'num_edges':
                print 'num_edges='+str(graph.num_edges())
            elif cmd == 'add_edge':
                v1 = int(tokens[1])
                v2 = int(tokens[2])
                graph.add_edge(v1, v2)
            elif cmd == 'vertex_degree':
                v = int(tokens[1])
                print 'vertex
