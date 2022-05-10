import threading
# Test threading daemon
import time


class Core(threading.Thread):
    def __init__(self, id=0, name="Core"):
        threading.Thread.__init__(self, name=name)
        self.setDaemon(True)
        self.id = id

    def run(self):
        while True:
            time.sleep(1)


if __name__ == "__main__":
    c = Core()
    s = c.start()
    time.sleep(2)
    print(s)
    c.start()


# Test for exception
"""
try:
    if True:
        raise Exception('raised')
except Exception as e:
    print(e)
"""

print("code finished...")
