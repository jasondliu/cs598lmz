import socket
# Test socket.if_indextoname, socket.if_nameindex, socket.if_nametoindex
if sys.platform in ('win32', 'darwin'):
    import errno
    raise ImportError("Can't run this test on %s" % sys.platform)

if_indextoname = socket.if_indextoname
if_nameindex = socket.if_nameindex
if_nametoindex = socket.if_nametoindex

class InterfaceError(Exception):
    pass

def test():
    nameindices = if_nameindex()
    if not nameindices:
        raise InterfaceError("No interfaces known to the system")

    first_name, first_index = nameindices[0]
    last_name, last_index = nameindices[-1]

    assert first_index <= last_index

    indices = set(index
                  for name, index in nameindices
                  if if_indextoname(index) == name)

    if not indices:
        raise InterfaceError("No interfaces known to the system")

    first_index = min(indices)
    last_
