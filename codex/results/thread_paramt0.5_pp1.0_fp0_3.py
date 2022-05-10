import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from a separate thread!\n")).start()

import concurrent.futures
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future = executor.submit(lambda: sys.stdout.write("Hello from a separate thread!\n"))
    future.result()

import multiprocessing
multiprocessing.Process(target=lambda: sys.stdout.write("Hello from a separate process!\n")).start()

with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    future = executor.submit(lambda: sys.stdout.write("Hello from a separate process!\n"))
    future.result()

import asyncio
async def hello():
    await asyncio.sleep(1)
    sys.stdout.write("Hello from a separate coroutine!\n")
    await asyncio.sleep(1)

asyncio.run(hello())

async def hello():
    await asyncio.sleep(1
