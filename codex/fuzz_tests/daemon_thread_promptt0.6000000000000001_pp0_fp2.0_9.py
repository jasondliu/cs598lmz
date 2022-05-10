import threading
# Test threading daemon

class Thread(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.daemon = True

    def run(self):
        print('starting')
        time.sleep(3)
        print('ending')

t = Thread(target=lambda: 1+1)
t.start()
print('started')
time.sleep(1)

print(t.is_alive())
time.sleep(5)
print(t.is_alive())
