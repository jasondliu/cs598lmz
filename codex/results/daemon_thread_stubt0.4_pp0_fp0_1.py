import sys, threading

def run():
    while True:
        sys.stdout.write("\r%s" % threading.current_thread().name)
        sys.stdout.flush()
        time.sleep(1)

for i in range(5):
    t = threading.Thread(target=run)
    t.start()
