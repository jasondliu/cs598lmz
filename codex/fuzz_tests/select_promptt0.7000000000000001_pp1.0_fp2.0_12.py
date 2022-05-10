import select
# Test select.select
import socket
import time

def test_select():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(5)
    port = s.getsockname()[1]
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(('localhost', port))
    s3, addr = s.accept()
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Test situation where all fds are ready for reading
        # and writing.
        w = select.select([s3, s2], [s3, s2], [])
        # Ensure we got the results we expected.
        assert sorted(w[0]) == [s2, s3]
        assert sorted(w[1]) == [s2, s3]
        # Now check that we didn't get any unexpected exceptions.
        assert not w[2]

       
