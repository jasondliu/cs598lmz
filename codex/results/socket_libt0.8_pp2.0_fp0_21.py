import socket
import threading
import time


def MessageSend(mySocket,ID):
	
	toSend = input()
	if toSend:
		mySocket.send(bytes(ID+": "+toSend,"UTF-8"))
		
	return 1

def CheckMessages(mySocket,ID):
 
	message = mySocket.recv(1024)
	if message:
		print(message.decode("UTF-8"))
	
	return 1

#Declarations

mySocket = socket.socket()
mySocket.connect(('127.0.0.1',12345))
readMessage = 1

ID = input("Enter ID : ")
mySocket.send(bytes(ID,"UTF-8"))

#Start Threads

_thread.start_new_thread(MessageSend,(mySocket,ID))
_thread.start_new_thread(CheckMessages,(mySocket,ID))

while readMessage:
	pass
