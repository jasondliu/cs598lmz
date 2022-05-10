import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())

def run_in_main():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())

def main():
    sys.stdout.write('Hello from thread %s\n' % threading.current_thread())
    t = threading.Thread(target=run)
    t.start()

    t.join()
    run_in_main()

main()
