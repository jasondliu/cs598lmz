import threading
# Test threading daemon

# a simple function
def function(i):
    print 'function called by thread %i\n' % i
    return

# create threads
threads = []
for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()

# wait for threads to finish
for i in threads:
    i.join()

# import threading
# import time
# import random
#
# def myfunc(i):
#     print "sleeping 5 sec from thread %d" % i
#     time.sleep(5)
#     print "finished sleeping from thread %d" % i
#
# for i in range(10):
#     t = threading.Thread(target=myfunc, args=(i,))
#     t.start()
#
# print "finished"
