import sys, threading

def run():
    try:
        while True:
            sys.stdout.write('%s\n' % threading.current_thread().name)
            sys.stdout.flush()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=run)
        t.setDaemon(True)
        t.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        sys.exit(0)
