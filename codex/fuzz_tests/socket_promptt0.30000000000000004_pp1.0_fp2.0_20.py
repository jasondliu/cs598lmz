import socket
# Test socket.if_indextoname()

def test_if_indextoname(ifname):
    try:
        idx = socket.if_nametoindex(ifname)
    except OSError:
        print("%s: no such interface" % ifname)
        return
    name = socket.if_indextoname(idx)
    print("%s: idx=%d name=%s" % (ifname, idx, name))

test_if_indextoname("lo")
test_if_indextoname("eth0")
test_if_indextoname("eth1")
test_if_indextoname("eth2")
test_if_indextoname("eth3")
test_if_indextoname("eth4")
test_if_indextoname("eth5")
test_if_indextoname("eth6")
test_if_indextoname("eth7")
test_if_indextoname("eth8")
test_if_indextoname("eth9")
test_if_indext
