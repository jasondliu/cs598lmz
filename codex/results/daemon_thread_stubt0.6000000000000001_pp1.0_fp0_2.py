import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())

def main():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    sys.stdout.write('thread %s done\n' % threading.current_thread())

if __name__ == '__main__':
    main()
