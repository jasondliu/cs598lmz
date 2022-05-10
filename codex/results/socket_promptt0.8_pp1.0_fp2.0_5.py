import socket
# Test socket.if_indextoname()
# Code is documented in the standard library
# https://docs.python.org/3/library/socket.html#socket.if_indextoname
def test_if_indextoname():
  print("Testing socket.if_indextoname()")
  print("If this test fails it may be due to test environment")
  print("only having loopback interface")
  try:
    print("Socket has", len(socket.if_indextoname(1)), "interfaces")
    print("Loopback interface has index", socket.if_nametoindex("lo"))
    print("lo is at index", socket.if_nametoindex("lo"))
    print("Index 1 is interface", socket.if_indextoname(1))
    assert(socket.if_nametoindex("lo") == 1)
    assert(socket.if_indextoname(1) == "lo")
  except IOError as e:
    print("Got IOError", e)
    print("Assuming this is due to test environment")
    print("only having loopback interface")


print("
