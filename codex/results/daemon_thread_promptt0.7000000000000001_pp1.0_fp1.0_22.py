import threading
# Test threading daemon
def thread_function(name):
    print ("Thread %s: starting" % name)
    time.sleep(2)
    print ("Thread %s: finishing" % name)

print ("Main    : before creating thread")
x = threading.Thread(target=thread_function, args=(1,), daemon=False)
print ("Main    : before running thread")
x.start()
print ("Main    : wait for the thread to finish")
# x.join()
print ("Main    : all done")


# def worker():
#     """thread worker function"""
#     print('Worker')
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()
