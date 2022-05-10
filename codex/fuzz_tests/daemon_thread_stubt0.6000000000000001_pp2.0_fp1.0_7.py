import sys, threading

def run():
    while True:
        f = open("/etc/passwd")
        lines = f.readlines()
        f.close()
        time.sleep(1)

for i in xrange(5):
    t = threading.Thread(target=run)
    t.start()
