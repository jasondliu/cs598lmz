import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

# Install signal handler
signal.signal(signal.SIGALRM, handler)

# Set the first alarm
handler()
I_STATS = {0: 0, 1: 0, 2:0}


class Player(Actor):
    def __init__(self, env, name, pipe_in, pipe_out, player_id):
        self.env = env
        self.name = name
        self.pipe_in = pipe_in
        self.pipe_out = pipe_out
        self.id = player_id
        self.actions = {
            'CONNECT': self._connect,
            'REQUEST': self._request,
            'DISCONNECT': self._disconnect
        }
        self.buffer_pool_size = 25
        self.buffers = queue.Queue()
        self.response = None
        self.asleep = False


    def run(self):
        while True:
            try:
                message = self.pipe_in.get()
                self
