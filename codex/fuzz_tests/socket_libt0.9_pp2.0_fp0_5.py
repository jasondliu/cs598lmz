import socket
import asyncio
from typing import Optional, List, Tuple

from ffxiv_alert import config, discord

async def create_server():
    server = await asyncio.start_server(
        handle_connection,
        config.host, config.port, loop=config.loop, ssl=None
    )
    return server

async def handle_connection(reader, writer):
    addr = writer.get_extra_info('peername')
    print('Received connection from', addr)

    try:
        async for msg in read_messages(reader):
            await notify_discord(msg)

    except asyncio.IncompleteReadError:
        pass

    print('Connection lost', addr)

async def read_messages(reader):
    while True:
        try:
            size = await reader.readexactly(8)
            size = int.from_bytes(size, byteorder='little')
        except (ConnectionError, asyncio.IncompleteReadError):
            # Client disconnected before sending a valid size. IncompleteReadError is raised by `
