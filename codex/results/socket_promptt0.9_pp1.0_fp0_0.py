import socket
# Test socket.if_indextoname()
# socket.if_indextoname() requires root permission, and on OpenBSD, it is broken issue.
indextoname_test_port = [
    (5, 8080),   # http port
    (5, 22),     # ssh port
    (2, dst_port),   # common port range
    (2, 30303)  # ethereum port
]


def get_ip_port_pairs():
    protocol = socket.IPPROTO_TCP
    for p in indextoname_test_port:
        yield p

@pytest.mark.parametrize('index, port', get_ip_port_pairs())
def test_if_indextoname(index, port):
    app = TestApp(picotcp.picotcp_lib)
    iface = app.lib.new_interface()
    iftype = app.lib.pico_string_to_ipv4('0.0.0.0')
    assert app.lib.pico_ipv4_link_add(iface, iftype, None
