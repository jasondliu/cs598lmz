import sys, threading

def run():
    print('run from thread %s' % threading.current_thread())

def main():
    t = threading.Thread(target=run)
    t.start()

if __name__ == '__main__':
    print('is main thread? %s' % threading.current_thread().is_alive())
    main()
    print('is main thread? %s' % threading.current_thread().is_alive())
