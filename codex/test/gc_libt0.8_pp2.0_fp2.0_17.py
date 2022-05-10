import gc, weakref

class Counter(object):
    def __init__(self):
        self.counter = 0

    def __call__(self):
        self.counter += 1
        return self.counter

counter = Counter()

