import io
class File(io.RawIOBase):
    def write(self, b):
        print("write", b)
    def read(self, size=-1):
        return b"hello"
f = File()
f.write(b"hello")

f.tell()

f.fileno()

f.flush()

f.isatty()

print(f.readable())

print(f.seekable())

#f.readinto()

#f.readline()

print(f.read())

print(f.read(3))


# Asynchronous I/O
import asyncio
import os

async def wait_5(event):
    await asyncio.sleep(5)
    event.set()

def wait_5_coroutine():
    e = 5
    event = asyncio.Event()
    print(dir(event.set()))
    event.set()
    return wait_5(event)

#asyncio.run(wait_5_coroutine())

async def file_reader(filename):
    print("read from a file {}".
