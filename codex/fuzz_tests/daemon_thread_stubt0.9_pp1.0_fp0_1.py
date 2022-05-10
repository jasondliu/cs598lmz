import sys, threading

def run():
    for i in range(3):
        print(threading.currentThread().getName())

t1 = threading.Thread(target=run)
# there are two ways thread can be named
#t1 = threading.Thread(target=run, name="thread-1")
#t1.setName("thread-1")
#t1.start()
#t1.join()
#print(threading.activeCount())
#print(threading.currentThread().getName())
#print(threading.currentThread().getName())
#print(threading.currentThread())
#print(threading.currentThread().isDaemon())
print(t1.isDaemon())
t1.daemon = True
t1.start()
#t1.run()
t1.join()
print(t1.isDaemon())
print(threading.enumerate())
