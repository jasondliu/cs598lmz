import select
# Test select.select()
def test_select():
    import select
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, 0))
    s.listen(1)
    port = s.getsockname()[1]
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((HOST, port))
    s3, addr = s.accept()
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # We can pass an open file descriptor...
        r, w, e = select.select([s3], [s3], [s3], 1)
        if s3 not in r or s3 not in w or s3 not in e:
            raise TestFailed, "Failed on first select"
        # ...or a socket object
        r, w, e = select.select([s4], [s4], [s4], 1)
        if s4 in r or s
