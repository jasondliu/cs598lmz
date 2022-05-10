import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=run)
t.start()

time.sleep(5)

t.join()
</code>

