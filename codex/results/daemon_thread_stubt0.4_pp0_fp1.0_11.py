import sys, threading

def run():
    print "Running"
    sys.stdout.flush()
    time.sleep(2)
    print "Done"
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

print "Waiting for thread to finish"
sys.stdout.flush()
t.join()
print "Thread finished"
sys.stdout.flush()
