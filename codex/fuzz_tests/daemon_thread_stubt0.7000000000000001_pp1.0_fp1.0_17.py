import sys, threading

def run():
    while True:
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        sys.stdout.write('\r{0:3} {1:3} {2:3}'.format(x, y, z))
        sys.stdout.flush()
        time.sleep(0.1)

thread = threading.Thread(target=run)
thread.start()

while True:
    # Do some other work here
    time.sleep(10)
</code>

