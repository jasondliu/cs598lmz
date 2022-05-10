import sys, threading

def run():
    sys.stdout.write('hello ')
    time.sleep(1)
    sys.stdout.write('world')

print('hello', end='', flush=True)
t = threading.Thread(target=run)
t.start()
time.sleep(2)
prin
