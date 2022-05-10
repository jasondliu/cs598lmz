import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())

def main():
    threading.Thread(target = run).start()
    threading.Thread(target = run).start()

if __name__ == '__main__':
    main()
