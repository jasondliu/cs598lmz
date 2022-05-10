import sys, threading

def run():
    while True:
        print(threading.enumerate())
        time.sleep(0.1)
threading.Thread(target=run).start()
time.sleep(1)
for i in range(100):
    t = threading.Thread(target=lambda: sys.stdout.write('.'))
    t.start()
</code>

