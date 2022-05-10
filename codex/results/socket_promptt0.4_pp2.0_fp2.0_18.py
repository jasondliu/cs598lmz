import socket
# Test socket.if_indextoname()
#
# This is a test for https://github.com/micropython/micropython/issues/4579
#
# Author: Peter Hinch
# Copyright Peter Hinch 2020 Released under the MIT license

import uasyncio as asyncio
import usocket as socket

async def test():
    print('\nTest socket.if_indextoname()')
    try:
        print(socket.if_indextoname(0))
    except OSError as e:
        print('Expected failure:', e)

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
