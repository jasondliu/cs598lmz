import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, val):
        threading.Thread.__init__(self)
        self.val = val
    def run(self):
        for i in range(1, self.val):
            print("Value ", i)

t = MyThread(5)
t.start()

print("The main program continues to run in foreground.")

print("While the counte runs in thread.")

t.join()

print("Main program waited until thread was complete.")
