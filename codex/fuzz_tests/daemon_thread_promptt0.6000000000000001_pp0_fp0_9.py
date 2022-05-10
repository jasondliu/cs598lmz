import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html#threading.Thread.daemon
# "A daemon thread will shut down immediately when the program exits."
# https://www.geeksforgeeks.org/python-daemon-threads/
# "It is a thread that runs in the background and does not affect the execution of the main program."


# Subclassing threading.Thread
# https://docs.python.org/3/library/threading.html#thread-objects
# https://www.tutorialspoint.com/python3/python_multithreading.htm
# https://www.tutorialspoint.com/python3/python_multithreading.htm
class MyThread(threading.Thread):
    def run(self):
        test = 0
        while True:
            print(test)
            test += 1


threads = []
for i in range(5):
    t = MyThread()
    t.start()
    threads.append(t)

for t in threads:
    t.join()
