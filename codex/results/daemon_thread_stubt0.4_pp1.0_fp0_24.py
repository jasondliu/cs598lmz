import sys, threading

def run():
    while True:
        sys.stdout.write('%s\n' % threading.current_thread().name)
        sys.stdout.flush()

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('%s\n' % threading.current_thread().name)
