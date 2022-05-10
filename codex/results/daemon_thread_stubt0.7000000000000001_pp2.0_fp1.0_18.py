import sys, threading

def run():
    loop = asyncio.get_event_loop()
    loop.run_forever()

def get_event_loop():
    if sys.version_info[:2] < (3, 7):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()
    return loop

def main():
    loop = get_event_loop()
    loop.run_until_complete(asyncio.gather(
        listen(loop), 
        server(loop), 
        client(loop)
    ))

async def listen(loop):
    await asyncio.start_server(server_handler, '127.0.0.1', 8888, loop=loop)

async def server_handler(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r
