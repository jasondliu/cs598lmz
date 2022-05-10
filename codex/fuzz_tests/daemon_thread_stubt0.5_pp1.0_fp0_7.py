import sys, threading

def run():
    global is_running
    is_running = True
    while is_running:
        print('running')
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        is_running = False
        thread.join()
        print('Bye')
        sys.exit()
</code>

