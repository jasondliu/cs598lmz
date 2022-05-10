import signal
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

class Q:
    def __init__(self):
        self.a = []
    def __len__(self):
        return len(self.a)
    def put(self, b):
        self.a.append(b)
    def get(self):
        if len(self.a) == 0:
            return None
        return self.a.pop(0)
    def peek(self):
        if len(self.a) == 0:
            return None
        return self.a[0]

class G:
    last_ping = 0
    last_ping_value = 0
    last_ping_timestamp = None
    last_ping_elapsed = 0
    last_ping_elapsed_max = 0
    last_ping_elapsed_prev = 0
    last_ping_elapsed_prev_max = 0
    last_ping_elapsed_prev_prev = 0
    last_
