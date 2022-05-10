import socket
socket.if_indextoname(3)

# %%
# openvpn server
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.bind(('10.8.0.1', 1194))

# %%
while True:
    data, addr = s.recvfrom(65535)
    print(data)

# %%
