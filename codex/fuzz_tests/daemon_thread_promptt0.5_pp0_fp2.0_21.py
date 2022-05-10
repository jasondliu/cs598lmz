import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-non-daemon

# https://stackoverflow.com/questions/6920302/passing-arguments-to-python-threading-thread-start

class MyThread(threading.Thread):
    def __init__(self, number, callback):
        threading.Thread.__init__(self)
        self.number = number
        self.callback = callback

    def run(self):
        print("Thread {} started".format(self.number))
        self.callback(threading.get_ident(), self.number)
        print("Thread {} finished".format(self.number))


def my_callback(tid, number):
    print("Thread {} callback called".format(number))
    time.sleep(3)

threads = []

for i in range(5):
    thread = MyThread(i, my_callback)
    thread.daemon = True
    thread.start()
    threads.append(thread)

for thread
