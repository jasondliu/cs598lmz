import sys, threading

def run():
    global stop
    while not stop:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print('\nThread finished')

stop = False
thread = threading.Thread(target=run)
thread.start()

print('Press Enter to stop')
input()
stop = True

thread.join()
print('Finished')
