import selectors
import os
import json
from datetime import datetime
import time
from controllers import *
from models import *
from views import *


class Server:
    def __init__(self, host, port_num, op_system):
        self.host = host
        self.port_num = port_num
        self.encoding = 'utf-8'
        self.sel = selectors.DefaultSelector()
        self.hostSelf, self.hostOther = self.host.split(':')
        self.log = Log(os.path.join(os.getcwd(), 'logs', 'log_' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.txt'))
        self.users_database = Database('users')
        self.messages_database = Database('messages')
        self.rooms_database = Database('rooms')
        self.messages_database.update_dict('all', 'room_id')
