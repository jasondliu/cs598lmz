import socket
socket.if_indextoname(1)

#Import the UDP module
import UDP

#Initialize the UDP object
udp = UDP.UDP()

#Get the IP and Port
ip = udp.getIP()
port = udp.getPort()

#Create the socket
s = udp.createSocket()

#Bind the socket to the IP and Port
udp.bindSocket(s, ip, port)

#Receive data from the socket
data = udp.recvData(s)

#Print the data
print data

#Close the socket
udp.closeSocket(s)

#Print the IP and Port
print ip, port
