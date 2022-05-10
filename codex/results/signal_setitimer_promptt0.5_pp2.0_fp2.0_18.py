import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, lambda x,y: print('SIGALRM'))
signal.pause()

# Test signal.setitimer() and threading.Thread
import time
import threading

def thread_func(t):
    time.sleep(t)
    print('thread_func(%s) done' % t)

t = threading.Thread(target=thread_func, args=(1,))
t.start()

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, lambda x,y: print('SIGALRM'))
signal.pause()

# Test signal.setitimer() and multiprocessing.Process
import time
import multiprocessing

def thread_func(t):
    time.sleep(t)
    print('thread_func(%s)
