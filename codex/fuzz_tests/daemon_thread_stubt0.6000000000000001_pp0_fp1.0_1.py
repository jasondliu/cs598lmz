import sys, threading

def run():
    while True:
        m = sys.stdin.readline()
        if len(m) == 0:
            break
        print len(m)

t = threading.Thread(target = run)
t.start()

while True:
    m = sys.stdin.readline()
    if len(m) == 0:
        break
    print len(m)
