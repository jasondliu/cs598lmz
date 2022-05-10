import sys, threading

def run():
    col = 1
    while col < 100:
        sys.stdout.write("\r%d" % col)
        sys.stdout.flush()
        col += 1

th = threading.Thread(target=run)
th.start()

while True:
    print(" *", end='')
