import threading
# Test threading daemon mode
def thread_test():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

print("thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=thread_test, name='LoopThread')
t.setDaemon(True)
t.start()
t.join()
print("thread %s ended." % threading.current_thread().name)
