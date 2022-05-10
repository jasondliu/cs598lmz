import socket
socket.if_indextoname(6)
socke.if_nameindex()
# import socket
import nacl.public
server_key = nacl.public.PrivateKey.generate()
client_key = nacl.public.PrivateKey.generate()
]
server_public_key = server_key.public_key
client_public_key = client_key.public_key
shared_secret = server_key.shared_key(client_public_key)
print(shared_secret)
print(server_public_key)
print(server_key)
print(client_key)
