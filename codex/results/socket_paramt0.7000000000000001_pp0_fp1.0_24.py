import socket
socket.if_indextoname(3)

print("Active interfaces:")
for i in netifaces.interfaces():
    if i == 'lo':
        continue
    iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    if iface != None:
        for j in iface:
            print("Interface %s has address %s" % (i, j['addr']))
