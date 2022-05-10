import socket
socket.if_indextoname('0')

# In[2]:

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(address)
    clientsocket.send(bytes("welcome to the server!","utf-8"))
    clientsocket.close()
