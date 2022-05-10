import gc, weakref

class Object(object):
    def __init__(self):
        self.weak = weakref.ref(self)
        self.callback = lambda _: None

    @staticmethod
    def __weak_callback__(self_ref):
        self = self_ref()
        if self is not None:
            self.callback(self)
            del self.callback

    def register_callback(self, callback):
        self.callback = callback
        return self.weak

    def delete_callback(self):
        self.callback = lambda _: None


if __name__ == "__main__":
    a = Object()
    b = Object()
    b.callback = a.register_callback
    a.delete_callback()
    del a
    gc.collect()
