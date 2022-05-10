import sys, threading

def run():
    sys.stdout.write('\n')
    sys.stdout.flush()
    while True:
        sys.stdout.write('\r' + "".join(['.'] * (int(time.time() % 3) + 1)))
        sys.stdout.flush()
        time.sleep(0.5)

t = threading.Thread(target=run)
t.daemon = True
t.start()

print "Starting"
time.sleep(3)
print "Finished"
