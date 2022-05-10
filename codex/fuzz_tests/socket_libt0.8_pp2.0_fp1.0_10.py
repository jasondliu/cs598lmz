import socket
from sys import argv
import threading
import os
from multiprocessing import Process

host = argv[1]
port = argv[2]
users = {}

class ClientThread(threading.Thread):

    def __init__(self, ip, port, conn, workername):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        self.workername = workername

    def run(self):

        while 1:
            username = str(self.conn.recv(1024))
            message = str(self.conn.recv(2048))
            if message == "exit":
                break
            if username in users:
                to_user = users[username]
                to_user.conn.send(message)
            else:
                self.conn.send("Sorry, user is not online.")


class WorkerProcess(threading.Thread):

    def __init__(self, host, port, workername, conn):
        threading.Thread.__init__
