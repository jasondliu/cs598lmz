import sys, threading

def run():
    while 1:
        print "Hello World"
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while 1:
    print "Goodbye World"
    time.sleep(1)
</code>

