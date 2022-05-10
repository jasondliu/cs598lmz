import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        while True:
            time.sleep(2)
            print(self.id)

for i in range(5):
    t = MyThread(i)
    t.daemon = True
    t.start()
