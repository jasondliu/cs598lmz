import socket
# Test socket.if_indextoname()
import test.test_support

if not hasattr(socket, 'if_indextoname'):
    raise test.test_support.TestSkipped("if_indextoname() not found")

# Get the name of the first network interface
name = socket.if_indextoname(1)
# Check that it is a string
if not isinstance(name, str):
    raise test.test_support.TestFailed("if_indextoname() did not return a string")
# Check that the name is not empty
if not name:
    raise test.test_support.TestFailed("if_indextoname() returned an empty string")

# Check that the name is not too long
if len(name) > 255:
    raise test.test_support.TestFailed("if_indextoname() returned a string that is too long")

# Check that the name is a valid interface name
if not name.startswith("lo") and not name.startswith("eth") and not name.startswith("wlan"):
    raise test.
