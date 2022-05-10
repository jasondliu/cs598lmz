import sys, threading

def run():
    while True:
        sys.stdout.write('Hello from Python!\n')
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()
