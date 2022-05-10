import sys, threading

def run():
    for i in range(100000):
        pass

threads = []
num_threads = 8

for i in range(num_threads):
    t = threading.Thread(target = run)
    t.daemon = True
    t.start()
    t.join()

print "done"
