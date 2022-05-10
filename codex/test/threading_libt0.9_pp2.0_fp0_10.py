import threading
threading.stack_size(1024*1024*10)

def handler(cls, method, body):
    cls.method_map[method](cls, body)

def handle_start(self, body):
    self.listen = []
    self.listen.append(body)
    print(self.listen)

def handle_stop(self, body):
    self.monitor = []
    self.monitor.append(body)
    print(self.monitor)

def handle_error(self, body):
    print(body)

class Consumer(object):
    def __init__(self, group, servers):
        self.group = group
        self.servers = servers
        global consumer
