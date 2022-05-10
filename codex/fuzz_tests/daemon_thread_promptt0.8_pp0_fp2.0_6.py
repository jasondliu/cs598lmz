import threading
# Test threading daemon
import time

class Daemon(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Daemon, self).__init__(*args, **kwargs)
        self.daemon = True

def func(name):
    print("{} : start".format(name))
    for i in range(10):
        time.sleep(1)
        print("{} : {}".format(name, i))
    print("{} : end".format(name))

if __name__ == '__main__':
    print("start")
    t = Daemon(target=func, args=("test",))
    t.start()
    print("end")
