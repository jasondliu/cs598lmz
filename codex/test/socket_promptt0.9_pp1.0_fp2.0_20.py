import socket
# Test socket.if_indextoname()

num_interfaces = 5
assert os.socket(socket.AF_INET, socket.SOCK_DGRAM) == os.socket(socket.AF_INET, socket.SOCK_DGRAM)

indices = []
for i in range(num_interfaces):
    name = "lo%d" % i
    index = socket.if_nametoindex(name)
    socket.if_indextoname(index)
    indices.append(index)
indices.sort()

print("iterating through all indices")
curr_index = 0
for i in range(num_interfaces + 1):
    index = socket.if_nameindex()[i][0]
    assert index == int(indices[curr_index])
    curr_index += 1
# Test socket.if_nameindex()
for name, index in socket.if_nameindex():
    socket.if_indextoname(index)
# Test socket.if_nameindex() with a simple number
