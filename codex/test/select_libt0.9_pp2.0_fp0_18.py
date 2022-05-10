import select
import fcntl

class Euler:
    def __init__(self, fds, stdin, stdout, stderr, handlers=[], has_input=False):
        self.fds, self.stdin, self.stdout, self.stderr, self.handlers = fds, stdin, stdout, stderr, handlers
        self.values = [0 for _ in range(len(fds))]
        self.has_input = has_input

    def send(self, i, v):
        self.values[i] = v

    def clear(self, i):
        self.values[i] = 0

    def has_output(self):
        return any(self.values)

    def output(self):
        return self.values.index(next([v for v in self.values if v]))

