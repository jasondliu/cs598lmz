import threading
# Test threading daemon
import time


class TestThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        global g_num
        tmp = g_num
        time.sleep(1)
        g_num = tmp + 1
        print("---threading " + str(self.num) + "---g_num= " + str(g_num))


for i in range(10):
    testThread = TestThread(i)
    testThread.setDaemon(True)
    testThread.start()

print("main threading end!")
