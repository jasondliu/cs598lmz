import sys, threading

def run():
    global running
    running = True
    while running:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\n')

def cancel():
    global running
    running = False

t = threading.Thread(target=run)
t.start()
time.sleep(5)
cancel()
t.join()
</code>

