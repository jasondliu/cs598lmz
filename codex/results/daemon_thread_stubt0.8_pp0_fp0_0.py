import sys, threading

def run():
    print('start')
    time.sleep(5)
    print('stop')

def timer(thread_name, delay, repeat):
    print(f'[+] Started Timer: {thread_name}')
    for i in range(repeat):
        time.sleep(delay)
        print(f'{thread_name}: {time.ctime(time.time())}')
    print(f'[+] Completed Timer: {thread_name}')

class ThreadingTimer(threading.Thread):
    def __init__(self, thread_name, delay, repeat):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.delay = delay
        self.repeat = repeat

    def run(self):
        timer(self.thread_name, self.delay, self.repeat)

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
