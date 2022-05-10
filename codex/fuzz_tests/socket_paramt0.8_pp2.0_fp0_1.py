import socket
socket.if_indextoname(i)

def get_label(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unkown"
        
for n, nbrs in g.adjacency():
    for nbr, _ in nbrs.items():
        g.add_edge(n, nbr, ip_src=g.nodes[n]["ip"], ip_dst=g.nodes[nbr]["ip"])

nx.set_node_attributes(g, "dns_src", {n: get_label(g.nodes[n]["ip"]) for n in g})
nx.set_node_attributes(g, "dns_dst", {n: get_label(g.nodes[n]["ip"]) for n in g})
nx.set_edge_attributes(g, "dns_src", {(n, nbr): get_label(ip_src) for n, nbr, ip_src in g.edges(data
