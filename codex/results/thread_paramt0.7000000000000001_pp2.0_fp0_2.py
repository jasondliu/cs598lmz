import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# with ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
def greet(name):
    print('hello ' + name)
with ThreadPoolExecutor(max_workers=3) as pool:
    list(map(pool.submit, [functools.partial(greet, name) for name in ['bob', 'julian', 'tim']]))

# threading.local
import threading

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        print('No value yet')
    else:
        print('value=%s' % val)

def worker(data):
    show_value(data)
    data.value = 5
    show_value(data)

local_data = threading.local()
show_value(local_data)
local_data.value = 15

