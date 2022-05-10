import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# Python 3.2
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=2)
def hello_from(msg):
    print('Hello from {}'.format(msg))
executor.submit(hello_from, 'Thread 1')
executor.submit(hello_from, 'Thread 2')

# Python 3.3
import asyncio
def hello_from(msg):
    print('Hello from {}'.format(msg))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    hello_from('Thread 1'),
    hello_from('Thread 2')
))
loop.close()

# Python 3.5
import asyncio
async def hello_from(msg):
    print('Hello from {}'.format(msg))
await asyncio.gather(
    hello
