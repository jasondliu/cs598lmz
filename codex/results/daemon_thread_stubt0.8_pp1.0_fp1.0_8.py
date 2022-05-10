import sys, threading

def run():
    print 'running'
    sys.stdin.readline()
    print 'done'

t = threading.Thread(target = run)
t.setDaemon(True)
t.start()

time.sleep(0.2)
print 'Telling thread to stop'
sys.stdout.flush()

# time.sleep(0.2)
# print 'Exiting'
# sys.stdout.flush()
