import select
# Test select.select() on a pipe

def test_select_pipe():
    r, w = os.pipe()
    try:
        for i in range(5):
            ret = select.select([r], [], [], 0.1)
            if ret[0]:
                os.read(r, 1)
    finally:
        os.close(r)
        os.close(w)

# Test select.select() on a file

def test_select_file():
    f = open(TESTFN, "wb")
    try:
        for i in range(5):
            ret = select.select([f], [], [], 0.1)
            if ret[0]:
                f.read(1)
    finally:
        f.close()
        os.remove(TESTFN)

# Test select.select() on a socket

def test_select_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    s.listen(1)
   
