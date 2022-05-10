import threading
# Test threading daemon
def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

start = time.time()

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f'Finished in {round(end-start, 2)} second(s)')

# Threading with daemon
start = time.time()

d = threading.Thread(target=do_something, daemon=True)

d.start()

end = time.time()

print(f'Finished in {round(end-start, 2)} second(s)')

# Test multiprocessing
import multiprocessing

import time

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

start = time
