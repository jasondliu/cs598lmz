import select
# Test select.select()

def test_select():
    # Test the select() function
    import select
    import socket

    # TODO: write a proper test
    # See Lib/test/test_select.py in the Python source tree
    # for an example of how this can be done.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    s2, addr = s.accept()
    s2.close()
    s.close()

if __name__ == "__main__":
    test_select()
