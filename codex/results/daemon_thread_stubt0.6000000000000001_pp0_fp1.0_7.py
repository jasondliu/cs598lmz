import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

time.sleep(10)
print('Finished')
