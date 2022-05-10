import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html
# https://stackoverflow.com/questions/190010/daemon-threads-explanation
# https://www.geeksforgeeks.org/python-threading-daemon-process-and-its-usage/
# https://pymotw.com/3/threading/

# Test threading event
# https://www.geeksforgeeks.org/python-threading-event-objects/

class MyThread(threading.Thread):
    def __init__(self, name, event):
        threading.Thread.__init__(self)
        self.name = name
        self.event = event

    def run(self):
        print("Starting " + self.name)
        while True:
            self.event.wait()
            print("%s received event." % self.name)
            self.event.clear()

def main():
    event = threading.Event()
    thread1 = MyThread("Thread-1", event)
    thread2 = MyThread
