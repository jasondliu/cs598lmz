import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

while True:
    line = sys.stdin.readline()
    if not line:
        break
    print 'You entered:', line
