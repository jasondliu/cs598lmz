import sys, threading

def run():
    print "running"
    time.sleep(10)
    print "done"

i = 0
while True:
    i += 1
    print "start", i
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    print "waiting"
    t.join(3) # or t.join(3)
    if t.is_alive():
        print "aborting"
        t._Thread__stop()
</code>
The output is:
<code>start 1
waiting
running
start 2
waiting
running
start 3
waiting
running
start 4
waiting
running
start 5
waiting
running
start 6
waiting
running
start 7
waiting
running
start 8
waiting
running
start 9
waiting
running
start 10
waiting
running
start 11
waiting
running
start 12
waiting
running
start 13
waiting
running
start 14
waiting
running
start 15
waiting
running
start 16
waiting
running
