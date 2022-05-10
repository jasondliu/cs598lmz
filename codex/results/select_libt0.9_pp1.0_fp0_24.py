import selectors.api as selectors
import socket
import time


scheduler = Scheduler()

tasks = []
task_ids = {}

class Client:
    def __init__(self, host, port, delay):
        self.host = host
        self.port = port
        self.delay = delay
        self.sel = selectors.DefaultSelector()
        self.conndata = None
        self.messages = []

        self.socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socks.setblocking(False)
        self.socks.connect_ex((self.host, self.port))
        self.sel.register(self.socks, selectors.EVENT_READ | selectors.EVENT_WRITE, data=self)


    def set_id(self, task_id):
        task_ids[self.socks.fileno()] = task_id

    def update(self, key, mask):
        scheduler.add_task(self.socks)
       
