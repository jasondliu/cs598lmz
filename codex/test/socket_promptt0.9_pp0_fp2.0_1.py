import socket
# Test socket.if_indextoname.
turtle_if = socket.if_indextoname(1)
print('Interface with index 1: {0}'.format(turtle_if))

# Test whether any interfaces have the string 'turtle' in them.
print('\n[*] Checking interfaces for \'turtle\'...')
for index in range(100):
    try:
        ifname = socket.if_indextoname(index)
    except IOError:
        break
    else:
        if 'turtle' in ifname:
            print('Interface with index {0} is called {1}'.format(
                index, ifname))

# Test socket.if_indextoname for network names.
net = socket.inet_aton("10.1.1.1")
print('\n[*] Looking up network name for 10.1.1.1...')
