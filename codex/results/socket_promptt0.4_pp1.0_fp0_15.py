import socket
# Test socket.if_indextoname()
import sys

from test import support

if not hasattr(socket, "if_indextoname"):
    raise support.TestSkipped("socket.if_indextoname() not available")

if_indextoname = socket.if_indextoname

def test_if_indextoname():
    # Test socket.if_indextoname()
    for index in range(256):
        try:
            name = if_indextoname(index)
        except OSError:
            pass
        else:
            if_indextoname(name)

def test_main():
    support.run_unittest(
        test_if_indextoname,
    )

if __name__ == "__main__":
    test_main()
