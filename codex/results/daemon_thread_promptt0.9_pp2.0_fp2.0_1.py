import threading
# Test threading daemon

def f():
    print ('this is the child thread')
    threading.get_ident()

def pid_thread_name():
    return "pid = {}, thread = {}".format(os.getpid(), threading.current_thread().name)

def f2():
    print('Daemon starting:', pid_thread_name())
    t = threading.current_thread()
    while getattr(t, 'do_run', True):
        print('Working:', pid_thread_name())
        time.sleep(1)
    print('Daemon exiting:', pid_thread_name())

def keep_working():
    print('I am not a daemon!')
    for n in range(10):
        time.sleep(1)
        print(f'Working {n}:', pid_thread_name())

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.
