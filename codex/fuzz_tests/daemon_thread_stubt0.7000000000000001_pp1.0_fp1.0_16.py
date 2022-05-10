import sys, threading

def run():
    while True:
        sys.stdout.write(" ")
        sys.stdout.flush()
        time.sleep(0.1)

th = threading.Thread(target=run)
th.daemon = True
th.start()

time.sleep(1)
print "..."
