import select
# Test select.select

def test_select():
    r, w, x = select.select([], [], [], 0.01)
    assert r == []
    assert w == []
    assert x == []

# Test socket.getaddrinfo

def test_getaddrinfo():
    addr = socket.getaddrinfo("127.0.0.1", 8080, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    assert addr[0][:3] == (2, 1, 6)
    assert addr[0][4][:2] == ("127.0.0.1", 8080)

# Test socket.gethostbyname

def test_gethostbyname():
    addr = socket.gethostbyname("localhost")
    assert addr == "127.0.0.1"

# Test socket.gethostname

def test_gethostname():
    name = socket.gethostname()
    assert isinstance(name, str)
    assert len(name) > 0
