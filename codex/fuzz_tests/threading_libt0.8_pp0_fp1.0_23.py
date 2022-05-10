import threading
threading.stack_size(2**27)
import sys
import graph_tool.all as gt
import time

def bfs(g, s, t):
    q = []
    q.append(s)
    check_arr = [0] * g.num_vertices()
    check_arr[s] = 1
    parent = [-1] * g.num_vertices()
    g.vertex(s).out_degree()

    while q:
        v = q.pop()
        if v == t:
            break
        for e in v.all_edges():
            e_vertex = int(e.target())
            if check_arr[e_vertex] == 0:
                q.append(g.vertex(e_vertex))
                check_arr[e_vertex] = 1
                parent[e_vertex] = v
            if(check_arr[t]):
                break
    path = []
    if check_arr[t] == 0:
        return path
    u = t
    while u != s:
