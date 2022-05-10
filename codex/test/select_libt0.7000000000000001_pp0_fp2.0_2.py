import selectors

class Selector:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.sel.register(sys.stdin, selectors.EVENT_READ)

    def process_events(self, loop):
        while True:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    continue
                callback = key.data
                callback(key.fileobj, mask, loop)

    def run(self, loop):
        try:
            self.process_events(loop)
        except KeyboardInterrupt:
            pass

    def register(self, sock, callback, data=None):
        self.sel.unregister(sock)
        self.sel.register(sock, selectors.EVENT_READ, (callback, data))

    def unregister(self, sock):
        self.sel.unregister(sock)
