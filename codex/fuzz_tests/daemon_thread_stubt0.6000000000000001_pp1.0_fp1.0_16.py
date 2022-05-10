import sys, threading

def run():
    while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        x = sys.stdin.readline()
        if len(x) == 0:
            break
        sys.stdout.write("!")
        sys.stdout.flush()

thr = threading.Thread(target=run, args=())
thr.start()

# this blocks
sys.stdin.readline()
