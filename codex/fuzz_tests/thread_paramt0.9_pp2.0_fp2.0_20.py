import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello")).start()
threading.Thread(target=lambda: sys.stdout.write("hell")).start()
threading.Thread(target=lambda: sys.stdout.write("helloo")).start()


#class SimpleThreads(threading.Thread):
#    def __init__(self, what, when, name=None):


#import threading, time
#def random_pause():
#    time.sleep(random.random()*0.1)
#    print("This was printed from the thread {0}".format(threading.current_thread().getName()))
#
#for i in range(5):
#    st = threading.Thread(target=random_pause)
#    st.start()


#import threading
#
#def print_time( threadName, delay):
#   count = 0
#   while count < 5:
#      time.sleep(delay)
#      count += 1
#      print ("%s: %s" % ( threadName, time.ctime(time.time())
