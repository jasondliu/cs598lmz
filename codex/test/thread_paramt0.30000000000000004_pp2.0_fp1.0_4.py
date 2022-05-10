import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# Python 3.4+
import asyncio
async def hello_world():
    print("Hello World!")

loop = asyncio.get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
loop.run_until_complete(hello_world())
loop.close()

# Python 3.5+
import asyncio
async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())  # will print "42".

# Python 3.5+
import asyncio
