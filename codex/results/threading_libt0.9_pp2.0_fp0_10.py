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
        consumer = KafkaConsumer(
             group_id=self.group, 
             bootstrap_servers=self.servers,
             enable_auto_commit=True,
             compute_latency=True,
             auto_offset_reset='earliest',
             consumer_timeout_ms=1000, 
             session_timeout_ms=30000, 

