import socket
socket.if_indextoname(2)

#create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the server
clientSocket.connect((serverName, serverPort))

#get message from user
message = input('Input lowercase sentence:')

#send message to server
clientSocket.send(message.encode())
#receive message from server
modifiedMessage = clientSocket.recv(1024)
#print the message
print(modifiedMessage.decode())

#close the socket
clientSocket.close()
