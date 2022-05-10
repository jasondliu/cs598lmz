import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

if_indextoname = socket.if_indextoname
if_nametoindex = socket.if_nametoindex

# Is there any way to deduce an interface name?

def check_if_indextoname(index):
    try:
        name = if_indextoname(index)
    except ValueError:
        print('if_indextoname(%d) failed' % index)
    else:
        print('if_indextoname(%d) => %r' % (index, name))
        index2 = if_nametoindex(name)
        print('if_nametoindex(%r) => %d' % (name, index2))
        if index != index2:
            print('if_indextoname(%d) and if_nametoindex(%r) are inconsistent!'
                  % (index, name))

# Now try to guess the index of a likely interface

def check_if_nametoindex(name):
    try:
        index = if_
