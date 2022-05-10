import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# This is the main function for the thread that runs the background tasks
def periodic_work(interval):
    while True:
        # Do your work here
        time.sleep(interval)

# Start a thread that will perform the periodic work
t = threading.Thread(target=periodic_work, args=(1,))
t.start()

# Do other work on the main thread
while True:
    print('hello')
    time.sleep(1)
