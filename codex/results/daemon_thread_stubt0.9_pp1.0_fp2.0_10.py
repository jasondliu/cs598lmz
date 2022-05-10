import sys, threading

def run():
    sys.stdout.write('Thread PID: %s\n' % os.getpid())
    sys.stdout.write('Thread _:   %s\n' % threading.current_thread())
    sys.stdout.write('Thread name:%s\n' % threading.current_thread().name)



# threading.Thread is a subclass of _thread.Thread in >=3.4
t = threading.Thread(target=run) # instantiate without invoking start
t.start() # start invokes the run() method in a separate thread of control

""" 

[.start() spawns a new thread in the same process,
t.join() waits for the thread to finish, 
and t.is_alive() checks whether the thread is still running.

You can also enumerate all running threads: threading.enumerate()

Occasionally you may want to launch a background thread that runs like a daemon. 
That is, it runs independently of the main application, 
and does not need to wait for the main thread to exit.
A daemon thread will shut down immediately when
