import threading
# Test threading daemon, Google instance tools
# ok, this runs, but doesn't actually do anything
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        print("Hello!")

for i in range(10):
    MyThread()

time.sleep(5)
print("Finished")

# demo of the above
def DoWork(num):
    print("Started working on {}".format(num))
    time.sleep(5)
    print("Finished working on {}".format(num))

# actually do the work in a separate thread
def ThreadPoolWork(num):
    t1 = threading.Thread(target=DoWork, args=[num])
    t1.start()

# spawn a thread for each job
for i in range(10):
    ThreadPoolWork(i)

# wait for each thread to finish (or just wait 2*(number of threads) seconds
for t in threading.enumerate
