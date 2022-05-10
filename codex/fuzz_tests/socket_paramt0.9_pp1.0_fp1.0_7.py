import socket
socket.if_indextoname(7)

## device etheraddr
out = client.run('ip link')
list_interfaces = [line.rstrip() for line in out]
for line in out:
    print('Device:',line.split(':')[1].strip())
    list_interfaces.append(line.split(': ')[1].strip())

## address 192.168.0.2/24
all_interfaces = client.interface
for interface in list_interfaces:
    print(interface.ipaddr)

# route
out = client.exec_command('ip route')
print(out)
