import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print("{} started!".format(self.name))
        time.sleep(random.choice([3,5,1]))
        print("{} finished!".format(self.name))

threads_list = []

for i in range(5):
    threads_list.append(MyThread("Thread-{}".format(i+1)))

for t in threads_list:
    t.setDaemon(True)
    t.start()

for t in threads_list:
    t.join()

print("All threads finished!")
