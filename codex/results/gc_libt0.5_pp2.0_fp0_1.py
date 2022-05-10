import gc, weakref
from collections import defaultdict

class GcTracker(object):
    def __init__(self):
        self.objects = defaultdict(int)
        self.objects_ref = {}
        self.tracked = set()
        self.old_cb = None
        self.enable()

    def enable(self):
        self.old_cb = gc.callbacks[:]
        gc.callbacks.append(self.track)

    def disable(self):
        gc.callbacks = self.old_cb

    def track(self, phase, info):
        for obj in gc.get_objects():
            if id(obj) in self.tracked:
                self.objects[(type(obj), id(obj))] += 1
                if self.objects[(type(obj), id(obj))] == 1:
                    self.objects_ref[(type(obj), id(obj))] = weakref.ref(obj)

    def __del__(self):
        self.disable()
        print('Found %d objects' % len(self.objects))
