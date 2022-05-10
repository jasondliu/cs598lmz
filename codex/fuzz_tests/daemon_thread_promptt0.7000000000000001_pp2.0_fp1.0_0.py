import threading
# Test threading daemon.
def myThread(n):
    print "thread " + str(n)
    time.sleep(0.2)
    print "thread " + str(n) + " end"

threads = []
i = 0
while (i < 10):
    t = threading.Thread(target=myThread, args=(i,))
    t.setDaemon(True)
    threads.append(t)
    i = i + 1

for t in threads:
    t.start()

j = 0
while (j < 10):
    print "main " + str(j)
    time.sleep(0.1)
    j = j + 1

print "main end"


import threading
# Test threading daemon.
def myThread(n):
    print "thread " + str(n)
    time.sleep(0.2)
    print "thread " + str(n) + " end"

threads = []
i = 0
while (i < 10):
    t = threading.Thread(target=myThread, args=(i,))
