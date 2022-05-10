import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/path/to/file.db')

class Reader(threading.Thread):
    def __init__(self, cond, q, name):
        super(Reader, self).__init__()
        self.cond = cond
        self.q = q
        self.name = name

    def run(self):
        with self.cond:
            self.cond.wait()
            print(self.name, ':', self.q.get())


class Writer(threading.Thread):
    def __init__(self, cond, q):
        super(Writer, self).__init__()
        self.cond = cond
        self.q = q

    def run(self):
        with self.cond:
            print('producer:', self.q.get())
            self.cond.notify_all()


def main():
    q = queue.Queue()
    q.put('first')
    q.put('second')
    cond = threading.Condition()
    r1 = Reader(cond, q, 'r1')
