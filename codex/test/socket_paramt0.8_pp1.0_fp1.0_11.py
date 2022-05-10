import socket
socket.if_indextoname(1)

#
# configure the various network interfaces
#
res = 0

for x in range(0, len(interfaces)):
    try:
        eth_name = socket.if_indextoname(x)
        res = ifconfig(eth_name, interfaces[x]['netmask']);
    except OSError:
        continue
    #if res == 0:
    #    print("Modifed interface: " + eth_name)
    #else:
    #    print("Failed to modify interface: " + eth_name)

#
# start the server
#
while True:
    print("Starting server...")
    try:
        registry.start()
    except KeyboardInterrupt:
        registry.stop()
        print("Caught keyboard interrupt. Stopping server.")
        sys.exit()
    except:
        continue
