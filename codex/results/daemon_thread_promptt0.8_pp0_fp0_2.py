import threading
# Test threading daemon settings
def myThread_1():
    print ("Start Threading:%s" % (time.ctime(time.time())))
    time.sleep(3)
    print ("End Threading:%s" % (time.ctime(time.time())))

threads = []
for i in range(5):
    threads.append(threading.Thread(target=myThread_1, name="Thread-%d" % (i+1), args=()))

for i in range(5):
    threads[i].start()
    threads[i].join() # wait for threading end
# print ("End Main Thread:%s" % (time.ctime(time.time())))

# threading lock
def myThread_2(arg1, arg2):
    print ("%s starts at %s" % (arg1, time.ctime(time.time())))
    time.sleep(arg2)
    print ("%s ends at %s" % (arg1, time.ctime(time.time())))

lock = threading.Lock()
thread
