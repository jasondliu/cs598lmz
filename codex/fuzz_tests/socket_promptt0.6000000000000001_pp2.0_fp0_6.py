import socket
# Test socket.if_indextoname()

print("\n=== Index to name ===")

print("\n*** Get the index of the 'lo' interface ***")
index = socket.if_nametoindex("lo")
print("index(lo) = %d" % index)

print("\n*** Get the name of interface with index %d ***" % index)
name = socket.if_indextoname(index)
print("name(%d) = %s" % (index, name))

print("\n*** Get the index of the 'eth0' interface ***")
index = socket.if_nametoindex("eth0")
print("index(eth0) = %d" % index)

print("\n*** Get the name of interface with index %d ***" % index)
name = socket.if_indextoname(index)
print("name(%d) = %s" % (index, name))

print("\n*** Get the name of interface with index -1 ***")
try:
    name = socket.if_indextoname(-1)
except Exception as e:

