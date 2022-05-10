import select
# Test select.select

def test_select():
    r, w, x = select.select([], [], [], 1.0)
    print(r, w, x)
    r, w, x = select.select([], [], [], 0.0)
    print(r, w, x)

# Test select.select
def test_select():
    import select
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    s.settimeout(2.0)
    try:
        s.connect(("www.python.org", 80))
    except socket.error as e:
        import errno
        if e.errno == errno.EWOULDBLOCK:
            print("socket timeout")
        else:
            print("socket error: %s" % e)
    else:
        print("connected")
        s.close()

# Test select.select
def test_select():
    import select
    import socket
    s = socket.socket(socket.AF_
