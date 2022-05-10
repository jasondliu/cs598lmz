import sys, threading

def run():
    while True:
        print "Hello World!"
        time.sleep(2)

t = threading.Thread(target=run)
t.daemon = True
t.start()

print "Press enter to quit..."
sys.stdin.readline()
