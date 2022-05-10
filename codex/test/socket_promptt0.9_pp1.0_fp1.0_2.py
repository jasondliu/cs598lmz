import socket
# Test socket.if_indextoname()
socket_names = [
    'lo',
    'eth0', 'eth1', 'eth2', 'eth3',
    'lo0', 'lo1', 'lo2', 'lo3',
    'wlan0', 'wlan1', 'wlan2', 'wlan3',
    'br-lan', 'br0', 'br1', 
]
for i in range(socket.if_nametoindex(socket_names[0]), socket.if_nametoindex(socket_names[-1])+1):
    socket_name = socket.if_indextoname(i)
    if not socket_name:
        continue
