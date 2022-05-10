import threading
# Test threading daemon
# Note that you can only use it on Global variables.
class TestThread(threading.Thread):
    def run(self):
        global testList
        for i in range(10000):
            time.sleep(0.0001)
            testList.append(i)

testList = []
testThreads = []

for i in range(500):
    testThreads.append(TestThread())
    testThreads[i].daemon = True # Make it a Daemon
    testThreads[i].start()
for i in range(500):
    testThreads[i].join()
len(testList)

# Test millis
class TestMillis(threading.Thread):
    def run(self):
        for i in range(10000):
            time.sleep(0.0001)
            a = millis()

testMillisThreads = []

for i in range(500):
    testMillisThreads.append(TestMillis())
    testMillisThreads[i].daemon = True # Make it a Daemon
    testMillisThreads
