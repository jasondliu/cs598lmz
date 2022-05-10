import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread\n")).start()
print("Hello from main\n")

#1.2 - Threading with a function argument
import sys, threading
def printHello(id):
    for i in range(10):
        sys.stdout.write("Hello from thread %d\n" % id)
for i in range(5):
    threading.Thread(target=printHello, args=(i,)).start()

#1.3 - Threading with a class
import sys, threading, time
class myThread (threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.name = name
        self.counter = counter
