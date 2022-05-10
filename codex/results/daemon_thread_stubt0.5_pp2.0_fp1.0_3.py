import sys, threading

def run():
    while True:
        sys.stdout.write('%s\n' % threading.current_thread().name)
        sys.stdout.flush()

def main():
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
