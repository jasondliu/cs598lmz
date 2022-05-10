import sys, threading

def run():
    global running
    running = True
    while running:
        time.sleep(1)
        print 'still alive'

thread = threading.Thread(target=run)
thread.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        running = False
        break
</code>
Or you could have a boolean variable in the thread and set it False when you want the thread to stop.

