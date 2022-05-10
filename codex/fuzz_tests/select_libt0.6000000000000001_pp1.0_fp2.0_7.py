import selectors

class Terminator(Exception):
    pass

class EventLoop:
    def __init__(self):
        self.stop = False
        self.selector = selectors.DefaultSelector()

    def add_task(self, task):
        self.selector.register(task.fileno(), selectors.EVENT_READ, task)

    def remove_task(self, task):
        self.selector.unregister(task.fileno())

    def run_forever(self):
        while not self.stop:
            for key, mask in self.selector.select():
                task = key.data
                try:
                    task.run_once()
                except Terminator:
                    self.stop = True
                except EOFError:
                    self.remove_task(task)

    def close(self):
        self.selector.close()

class Task:
    def __init__(self, coro):
        self.coro = coro
        self.step()

    def run_once(self):
        try:
            self.step()
