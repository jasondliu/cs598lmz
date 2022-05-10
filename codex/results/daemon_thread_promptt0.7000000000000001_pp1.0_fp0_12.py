import threading
# Test threading daemon

class Daemon(threading.Thread):
    def __init__(self, number, interval, counter):
        super(Daemon, self).__init__()
        self.number = number
        self.interval = interval
        self.counter = counter
        self.daemon = True

    def run(self):
        while True:
            c = self.counter.value
            print(self.number,c)
            c += 1
            time.sleep(self.interval)
            self.counter.value = c

d1 = Daemon(1, 1, multiprocessing.Value('i', 1))
d2 = Daemon(2, 0.5, multiprocessing.Value('i', 2))

d1.start()
d2.start()

d1.join()
d2.join()

print('Done')

# Daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, etc.) may not be released properly. If you want your threads to stop gracefully, make them non-daemonic and use a suitable signalling
