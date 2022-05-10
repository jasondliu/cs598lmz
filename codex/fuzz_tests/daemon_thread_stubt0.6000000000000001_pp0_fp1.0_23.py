import sys, threading

def run():
    print "thread start"
    
    while True:
        time.sleep(0.1)
        print "thread running"
        #sys.stdout.flush()

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

print "main start"

while True:
    time.sleep(0.1)
    print "main running"
    sys.stdout.flush()
