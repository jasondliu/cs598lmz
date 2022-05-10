import threading
# Test threading daemon
class Worker(threading.Thread):
    def run(self):
        print("Thread %s started" % self.getName())
        time.sleep(3)
        print("Thread %s finished" % self.getName())

def test_daemon():
    threads = [Worker() for i in range(10)]
    for t in threads:
        t.setDaemon(True)
        t.start()
    time.sleep(1)
    print("Main thread finished")

if __name__ == "__main__":
    test_daemon()
