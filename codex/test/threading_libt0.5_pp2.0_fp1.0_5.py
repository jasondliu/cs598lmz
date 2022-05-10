import threading
threading.stack_size(1024*1024*1024)

class Thread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)

def f(n):
    while True:
        print(n)
        n += 1

if __name__ == '__main__':
    t = Thread(f, 10)
    t.start()
