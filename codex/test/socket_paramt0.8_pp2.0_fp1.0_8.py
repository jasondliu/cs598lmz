import socket
socket.if_indextoname(3)

res = requests.get('https://api.ipify.org')

print(res.content)
