import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())

def test_thread():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())
    t = threading.Thread(target=run)
    t.start()
    t.join()
    sys.stdout.write('thread ended.\n')

if __name__ == '__main__':
    test_thread()
