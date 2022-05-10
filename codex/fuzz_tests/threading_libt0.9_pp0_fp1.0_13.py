import threading
threading.stack_size(67108864)

app = Flask(__name__)

class Counter(object):
    def __init__(self):
        pass

    def update(self):
        self.count = 1

    def counter(self):
        return self.count
