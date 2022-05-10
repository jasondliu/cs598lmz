import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # On Windows, test_if_indextoname() requires that you run the
    # script with Administrator privilege.
    for i in range(socket.if_nametoindex("lo0"), socket.if_nametoindex("lo0") + 2):
        try:
            print("{}: {}".format(i, socket.if_indextoname(i)))
        except OSError as ex:
            # OSError is expected on Windows
            if ex.errno != errno.EINVAL:
                raise
            print("{}: {}".format(i, ex))

if __name__ == "__main__":
    test_if_indextoname()
