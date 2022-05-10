import threading
# Test threading daemon
# threading.Thread(target = thread_job).start()
# threading.Thread(target = thread_job, daemon = True).start()
# threading.Thread(target = thread_job).start()
# threading.Thread(target = thread_job, daemon = True).start()

# time.sleep(5)
# print("Main Thread END")

# Test threading local
def thread_job():
    print("This is an added thread, number is %s" % threading.current_thread())
    # print(threading.local)

def thread_job2():
    print("This is an added thread, number is %s" % threading.current_thread())
    # print(threading.local)

# threading.Thread(target = thread_job).start()
# threading.Thread(target = thread_job2).start()

# Test threading lock
def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print("job1", A)
    lock.
