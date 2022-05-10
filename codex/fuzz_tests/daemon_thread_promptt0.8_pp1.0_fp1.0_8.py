import threading
# Test threading daemon
#def func():
#    for i in range(10):
#        print(threading.current_thread().name, i)
#    print(threading.active_count())
#    print(threading.enumerate())
#    print(threading.current_thread())
#
## Create two threads
#t1 = threading.Thread(name='consumer', target=func, daemon=True)
#t2 = threading.Thread(name='producer', target=func)

## Start threads
#t1.start()
#t2.start()
#
## Wait for threads to finish
#t1.join()
#t2.join()

# solution with threading
#def print_time(thread_name, delay, counter):
#    while counter:
#        time.sleep(delay)
#        print("%s: %s" % (thread_name, time.ctime(time.time())))
#        counter -= 1
#
## Create two threads
#t1 = threading.Thread(target=print_time, args=("Thread-1
