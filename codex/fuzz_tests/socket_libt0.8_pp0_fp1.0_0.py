import socket
import threading
import select
import time

HOST = 'localhost'
PORT = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)

#handles are the sockets
#tasks are the jobs
#jobExecutor are the threads
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def heartbeat(handle, task):
  request = str(task)
  request = request.encode()
  handle.sendall(request)
  data = handle.recv(1024)
  data = data.decode()
  return data

def download(handle, task):
  request = str(task)
  request = request.encode()
  handle.sendall(request)
  data = handle.recv(1024)
  data = data.decode()
  data = data.split("|")
  return data

def upload
