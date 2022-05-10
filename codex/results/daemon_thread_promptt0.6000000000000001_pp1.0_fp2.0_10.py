import threading
# Test threading daemon

class Threading(object):
    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            print('Doing something imporant in the background')
            time.sleep(self.interval)

Threading(1)

while True:
    print('Doing something important in the foreground')
    time.sleep(1)

print('Done')

# Test threading non-daemon

class Threading(object):
    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = False
        thread.start()

    def run(self):
        while True:
            print('Doing something imporant in the background')
            time.sleep(self.interval)

Threading(1)

while True:
