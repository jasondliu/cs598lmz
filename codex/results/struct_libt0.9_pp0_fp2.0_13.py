import _struct
import time
from queue import Queue
from threading import Thread
sys.path.append('..')
from message import MessageHeader, MessageX86, MessageARM


class ShellProcessor(Thread):
    CMDS = {
        0: 'cmd_exit_session'
    }

    TIMEOUT = 10
    BROADCAST_IP = '255.255.255.255'

    def __init__(self, client, addr):
        self.client = client
        self.addr = addr
        self.free_port = Queue()
        self.shell = None
        self.building = False
        super(ShellProcessor, self).__init__()

    def run(self):
        self.client.send('#> '.encode('utf-8'))
        while True:
            msg_header = MessageHeader.recv(self.client)
            if not msg_header:
                logging.info('Client session closed')
                break
            op = msg_header.get_cmd()
            if op not in ShellProcessor.CMDS:
                logging.info('Invalid
