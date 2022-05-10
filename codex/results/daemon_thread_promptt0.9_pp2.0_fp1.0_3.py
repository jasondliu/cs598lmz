import threading
# Test threading daemonic
# Set the thread to daemon
def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')
d = threading.Thread(name='daemon thread', target=worker)
d.setDaemon(True)

def non_daemon():
    print(threading.currentThread().getName(), 'Starting')
    print(threading.currentThread().getName(), 'Exiting')
t = threading.Thread(name='non-daemon thread', target=non_daemon)

d.start()
t.start()
d.join()
t.join()

#Daemonic threads will quit witout waiting the work done

#threading.Thread.join()
#The arguments to join specify a timeout. If the thread does not finish in the timeout
#seconds, join returns anyway

#Running code at specific intervals
#use threading.Timer
# set a periodic timer with a certain interval
# def hello():
#     print('Hello Timer!')
