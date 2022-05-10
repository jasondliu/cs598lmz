import socket
# Test socket.if_indextoname (LP: #512886)
def test_if_indextoname():
    try:
        socket.if_indextoname(1)
    except IOError as e:
        # This could fail if there is no such interface as 1.
        # The test is that the function is available, and that
        # when it fails, it raises an IOError (rather than segfaulting
        # or anything worse).
        assert_match(str(e), 'No such device')
