import socket
# Test socket.if_indextoname()

# FreeBSD supports at least 20 interfaces, but I don't have
# the hardware to test this.  So this test will pass if the
# OS supports at least 2 interfaces, which a reasonably modern
# Linux box should.

# Test 1
count = 0
for interface in socket.if_indextoname:
    count += 1

if count > 1:
    print(count, "interfaces found")
else:
    print(count, "interface found")
    raise TestFailed("Didn't find enough interfaces")

# Test 2
for interface in socket.if_indextoname:
    try:
        l = socket.if_indextoname[interface]
    except KeyError:
        raise TestFailed("Found invalid interface")

# Test 3
for interface in socket.if_indextoname:
    try:
        l = socket.if_indextoname[interface]
    except TypeError:
        raise TestFailed("Key# was not an integer")

# Test 4
index = 0
for li in socket.if_nametoindex.
