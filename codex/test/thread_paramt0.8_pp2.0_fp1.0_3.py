import sys, threading
threading.Thread(target=lambda: sys.stdout.write('→')).start()
threading.Thread(target=lambda: sys.stdout.write('←')).start()
threading.Thread(target=lambda: sys.stdout.write('↑')).start()
threading.Thread(target=lambda: sys.stdout.write('↓')).start()

# @see https://docs.python.org/3/library/asyncio-eventloop.html
import asyncio
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)

async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(
        print_nums()
    )

