import threading
threading.Thread(target=lambda x: x, args=(1,)).start()

# Importing asyncio and sys
import asyncio
import sys

# Defining the async method
async def myAsyncMethod():
    print("My async method")

# Getting the event loop and executing the method
loop = asyncio.get_event_loop()
loop.run_until_complete(myAsyncMethod())
loop.close()

# Importing the asyncio module
import asyncio

# Defining the async method
async def myAsyncMethod():
    print("My async method")

# Getting the event loop and executing the method
loop = asyncio.get_event_loop()
loop.run_until_complete(myAsyncMethod())
loop.close()

# Importing the asyncio module
import asyncio

# Defining the async method
async def myAsyncMethod():
    print("My async method")

# Getting the event loop and executing the method
loop = asyncio.get_event_loop()
loop.run_until_complete(myAsyncMethod())
loop.close()

