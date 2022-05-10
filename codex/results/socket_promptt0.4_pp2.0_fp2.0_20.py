import socket
# Test socket.if_indextoname()

def test_if_indextoname(dev, funcname):
    if_index = socket.if_nametoindex(dev)
    if_name = socket.if_indextoname(if_index)
    if if_name != dev:
        print(funcname + " failed")
        raise SystemExit

    print(funcname + " success")

if __name__ == '__main__':
    test_if_indextoname("lo", "test_if_indextoname")
