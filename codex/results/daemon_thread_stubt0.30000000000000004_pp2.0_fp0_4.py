import sys, threading

def run():
    while True:
        print "Hello World"
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

print "Press Ctrl+C to exit"

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
</code>

