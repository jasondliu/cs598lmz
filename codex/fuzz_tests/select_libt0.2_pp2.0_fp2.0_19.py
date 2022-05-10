import select
import socket
import sys
import threading
import time
import traceback

from . import _common
from . import _constants
from . import _errors
from . import _events
from . import _util
from . import _websocket_app
from . import _websocket_server

_logger = logging.getLogger(__name__)


class WebSocketServer(_websocket_server.WebSocketServer):
    """WebSocket server implementation.

    This class implements a WebSocket server.  The following example
    code creates a server that echoes back all received data to
    the client::

        import asyncio
        import websockets

        async def echo(websocket, path):
            async for message in websocket:
                await websocket.send(message)

        start_server = websockets.serve(echo, 'localhost', 8765)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    The server runs until Ctrl+C is pressed.

    :
