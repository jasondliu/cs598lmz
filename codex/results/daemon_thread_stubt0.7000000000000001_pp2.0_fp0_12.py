import sys, threading

def run():
    print "thread is running"
    print "thread's name is %s" % threading.current_thread().name
    print "thread's name is %s" % threading.current_thread().getName()
    print "thread's name is %s" % threading.currentThread().getName()
    print "thread's name is %s" % threading.currentThread().name
    print "thread's name is %s" % threading.current_thread().__class__

t = threading.Thread(target=run)
t.start()
t.join()

print "thread's name is %s" % threading.current_thread().name
print "thread's name is %s" % threading.current_thread().getName()
print "thread's name is %s" % threading.currentThread().getName()
print "thread's name is %s" % threading.currentThread().name
print "thread's name is %s" % threading.current_thread().__class__

# python is different from other languages that the object can not be created without an instance.

