import selectors, os, json
import time, sys

from chat_utils import *
import chat_group as grp
from chat_shared import propagate_timestamp

class Server:
    def __init__(self):
        self.new_clients = [] #list of new sockets of which the user id is not known
        self.logged_name2sock = {} #dictionary mapping username to socket
        self.logged_sock2name = {} # dict mapping socket to user name
        self.all_sockets = []
        self.group = grp.Group()
        #start server
        self.server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(SERVER)
        self.server.listen(5)
        self.all_sockets.append(self.server)
        #initialize policy database
        self.indices = {}
        self.policy_db = []
        read_policy_db()
        #initialize selectors
        self.sel = selectors.DefaultSelector()
       
