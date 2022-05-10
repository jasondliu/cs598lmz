import threading
# Test threading daemon
# https://stackoverflow.com/questions/3788208/python-threading-bug

class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"

for x in range(4):                                     # Four times...
    mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
    mythread.start()                                   # ...Start the thread
    time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another

# Output:
# Thread-1 started!
# Thread-1 finished!
# Thread-2 started!
# Thread-2 finished!
# Thread-3 started!
# Thread-3 finished!
# Thread-4 started!
# Thread-4 finished!


