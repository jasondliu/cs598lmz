import threading
# Test threading daemon
#
#

class ThreadWorker(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.running = True
        self.counter = 0
    def stop(self):
        self.running = False
    def run(self):
        while self.running:
            self.counter += 1
            print("Thread %s: %s" % (self.id, self.counter))
            time.sleep(1)

def main():
    threads = []
    for i in range(2):
        t = ThreadWorker(i)
        t.setDaemon(True)
        t.start()
        threads.append(t)

    time.sleep(5)
    print("Main thread exit")

if __name__ == "__main__":
    main()
