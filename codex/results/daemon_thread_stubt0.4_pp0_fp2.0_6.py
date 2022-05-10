import sys, threading

def run():
    while 1:
        sys.stdout.write('\r' + ' ' * 50 + '\r')
        sys.stdout.flush()
        sys.stdout.write('\r' + '*' * random.randint(0, 50))
        sys.stdout.flush()
        time.sleep(0.2)

t = threading.Thread(target=run)
t.start()

time.sleep(10)

t.join()
</code>

