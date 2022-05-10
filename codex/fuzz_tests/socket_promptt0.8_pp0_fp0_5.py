import socket
# Test socket.if_indextoname()
# If a NIC has multiple IP addresses, only one is listed in this function.
with open('/proc/net/route') as route_file:
    for line in route_file:
        route_info = line.split()
        if route_info[1] == '00000000':
            if_index = int(route_info[0], 16)
            if_name = socket.if_indextoname(if_index)
            #if_name = if_name[:5]
            print if_index, if_name
            break
