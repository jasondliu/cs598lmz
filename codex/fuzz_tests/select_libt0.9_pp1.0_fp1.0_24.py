import select
import socket
import threading
import pygame

class InputStream(threading.Thread):
	def __init__(self,threadID,serverIp,serverPort,serverName):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.serverIP = serverIp
		self.serverPort = serverPort
		self.serverName = serverName
		self.buffersize = 1024
		self.playOn = True
		self.inputSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	def run(self):
		self.inputSock.connect((self.serverIP,self.serverPort))
		self.inputSock.sendall(self.serverName.encode("utf-8"))
		self.inputSock.sendall("\n".encode("utf-8"))
		time.sleep(1)
		self.inputSock.sendall("READY".encode("utf-8"))
		print
