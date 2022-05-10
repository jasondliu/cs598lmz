import select
import random
import sys, string

class Chat:

    def __init__(self):
        self.conn_dict = {}
        self.buffer_dict = {}
        self.group_dict = {}

    def connect(self, conn, addr, conn_dict, buffer_dict, group_dict):
        user_id = conn.recv(1024).decode('utf-8')
        if user_id != 'USER' and len(user_id) <= 10 and len(user_id) >0:
            self.conn_dict[conn] = user_id
            self.buffer_dict[conn] = ''
            self.group_dict[conn] = 0
            print('%s has join the chat room' % (user_id))
            conn.send('SERVER: %s has join the chat room.'.encode('utf-8'))
        else:
            conn.send('ERR NOT USERNAME'.encode('utf-8'))

    def leave(self, conn, addr, conn_dict, buffer_dict, group_dict):
        user_
