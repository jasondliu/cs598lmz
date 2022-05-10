import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
        
    def run(self):
        print("Thread", self.num, "started")
        time.sleep(3)
        print("Thread", self.num, "finished")
        

for i in range(10):
    t = MyThread(i)
    t.setDaemon(True)
    t.start()
    
print("Main thread finished")

# Main thread finished
# Thread 0 started
# Thread 1 started
# Thread 2 started
# Thread 3 started
# Thread 4 started
# Thread 5 started
# Thread 6 started
# Thread 7 started
# Thread 8 started
# Thread 9 started

# Main thread finished
# Thread 0 started
# Thread 0 finished
# Thread 1 started
# Thread 1 finished
# Thread 2 started
# Thread 2 finished
# Thread 3 started
# Thread 3 finished
# Thread 4 started
# Thread 4 finished
# Thread 5 started
# Thread 5 finished
# Thread 6
