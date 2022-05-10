import threading
# Test threading daemon
# https://stackoverflow.com/questions/29306747/how-to-make-a-python-thread-terminate-when-the-main-program-ends
#
# Test threading.Event
# https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
#
# Test threading timer
# https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.5):
            print("MyThread")

stopFlag = threading.Event()
thread = MyThread(stopFlag)
thread.start()

time.sleep(3)
stopFlag.set()
thread.join()
