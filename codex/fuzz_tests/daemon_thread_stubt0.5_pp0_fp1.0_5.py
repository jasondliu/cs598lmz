import sys, threading

def run():
    while True:
        print('Hello from thread %s' % threading.current_thread().name)
        sys.stdout.flush()

def main():
    print('Hello from thread %s' % threading.current_thread().name)
    sys.stdout.flush()
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('Hello from thread %s' % threading.current_thread().name)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
