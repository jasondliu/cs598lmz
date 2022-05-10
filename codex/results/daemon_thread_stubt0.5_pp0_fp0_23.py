import sys, threading

def run():
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()
    for i in range(1, 50):
        sys.stdout.write("\x1b[%d;%dH" % (i, i))
        sys.stdout.write("%d" % i)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=run)
t.start()

for i in range(1, 50):
    sys.stdout.write("\x1b[%d;%dH" % (i, i))
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.1)
