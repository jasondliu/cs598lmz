import threading
# Test threading daemon
# https://stackoverflow.com/questions/19051796/python-threading-daemon-vs-none

class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.5):
            print("My Thread")

stopFlag = threading.Event()
thread = MyThread(stopFlag)
thread.start()

time.sleep(3)

stopFlag.set()
thread.join()

print("thread stopped")

# Test threading
# https://stackoverflow.com/questions/1191374/using-module-subprocess-with-timeout

# def run(cmd, timeout):
#     proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     poll_seconds = .250
#     deadline = time.time() + timeout
#    
