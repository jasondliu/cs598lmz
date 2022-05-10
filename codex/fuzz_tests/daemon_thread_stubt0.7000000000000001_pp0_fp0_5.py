import sys, threading

def run():
    t = threading.currentThread()
    print(t.getName(), 'starting')
    sys.stdout.flush()
    print(t.getName(), 'sleeping')
    time.sleep(1)
    print(t.getName(), 'exiting')
    sys.stdout.flush()

def main():
    threading.current_thread().setName('MainThread')
    print(threading.current_thread().getName(), 'starting')
    sys.stdout.flush()
    for i in range(3):
        t = threading.Thread(target = run)
        t.setName('Thread-' + str(i))
        t.start()
    print(threading.current_thread().getName(), 'exiting')
    sys.stdout.flush()

if __name__ == '__main__':
    main()
