import sys, threading

def run():
    # print(threading.currentThread())
    print(threading.current_thread())

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)

t1.start()
t2.start()

t1.join()
t2.join()
 
print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())
