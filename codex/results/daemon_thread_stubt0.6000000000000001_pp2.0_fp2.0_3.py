import sys, threading

def run():
    while True:
        print "thread"

t = threading.Thread(target = run)
t.start()

while True:
    print "main"
</code>

