import sys, threading

def run():
    while True:
        print "Hello"

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    print "World"
    time.sleep(1)
</code>

