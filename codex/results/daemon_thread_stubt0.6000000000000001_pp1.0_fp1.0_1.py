import sys, threading

def run():
    sys.stdout.write('Thread %s started\n' % threading.current_thread().name)
    sys.stdout.write('Thread %s ended\n' % threading.current_thread().name)

def test():
    sys.stdout.write('Main thread started\n')
    thread = threading.Thread(target=run, name='TestThread')
    thread.start()
    sys.stdout.write('Main thread ended\n')

if __name__ == '__main__':
    test()
</code>
Output:
<code>Main thread started
Thread TestThread started
Main thread ended
Thread TestThread ended
</code>

