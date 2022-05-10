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
