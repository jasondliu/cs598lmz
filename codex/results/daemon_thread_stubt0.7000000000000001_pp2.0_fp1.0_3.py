import sys, threading

def run():
    for i in range(100):
        sys.stdout.write('%s\n' % i)
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()

time.sleep(5)
</code>

