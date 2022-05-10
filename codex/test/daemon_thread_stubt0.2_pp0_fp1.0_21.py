import sys, threading

def run():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

print("thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=run, name="T1")
t.start()
t.join()
print("thread %s ended." % threading.current_thread().name)

# threading.Thread(target=run, name="T1").start()
# threading.Thread(target=run, name="T2").start()
# threading.Thread(target=run, name="T3").start()
# threading.Thread(target=run, name="T4").start()
# threading.Thread(target=run, name="T5").start()
