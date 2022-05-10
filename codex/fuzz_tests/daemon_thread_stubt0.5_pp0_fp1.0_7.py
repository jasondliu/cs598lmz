import sys, threading

def run():
    print('Hello from thread %s' % threading.current_thread().name)
    sys.stdout.flush()

def main():
    print('Hello from thread %s' % threading.current_thread().name)
    sys.stdout.flush()
    t = threading.Thread(target=run)
    t.start()

main()
