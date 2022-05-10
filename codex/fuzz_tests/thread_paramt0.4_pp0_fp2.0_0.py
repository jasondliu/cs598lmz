import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# Python 3.2+
from concurrent.futures import ThreadPoolExecutor
def hello_from(val):
    sys.stdout.write('Hello from {}\n'.format(val))

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(hello_from, range(5))

# Python 3.5+
import asyncio
async def hello_from(val):
    sys.stdout.write('Hello from {}\n'.format(val))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*[hello_from(i) for i in range(5)]))
loop.close()

# Python 3.5+
import asyncio
async def hello_from(val):
    sys.stdout.write('Hello from {}\n'.format(val))
