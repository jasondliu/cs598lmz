import gc, weakref, time

class Counter(object):
    _instances = 0
    _lost_references = []

    def __init__(self):
        self.count = 0
        Counter._instances += 1

    def perform_count(self):
        self.count += 1

    def __del__(self):
        Counter._instances -= 1

    @classmethod
    def print_lost_refs(cls):
        for ref in cls._lost_references:
            obj = ref()
            if obj:
                obj.perform_count()
        cls._lost_references = []

    @classmethod
    def print_instance_count(cls):
        return cls._instances


def default():
    a = weakref.WeakKeyDictionary()
    a['one'] = Counter()
    gc.collect()
    time.sleep(1)
    print('printing gc...')
    print(gc.garbage)
    print(Counter.print_lost_refs())
    print(Counter.print_instance_count())


