import sys, threading

def run():
    sys.stdout.write('\x07')
    sys.stdout.flush()

def set_timer(seconds):
    timer = threading.Timer(seconds, run)
    timer.start()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "USAGE: timer.py <seconds>"
    else:
        set_timer(int(sys.argv[1]))
        while True:
            time.sleep(1)
