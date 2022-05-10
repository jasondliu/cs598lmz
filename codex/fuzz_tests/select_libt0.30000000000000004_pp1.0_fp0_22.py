import select
import socket
import sys
import threading
import time

import pytest

from aiohttp import web
from aiohttp.connector import TCPConnector


@pytest.fixture
def loop(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(None)

    def fin():
        if not loop.is_closed():
            loop.call_soon(loop.stop)
            loop.run_forever()
            loop.close()
    request.addfinalizer(fin)
    return loop


@pytest.fixture
def make_app(loop):

    async def make_app(router):
        app = web.Application(loop=loop, router=router)
        return app
    return make_app


@pytest.fixture
def make_server(loop):

    async def make_server(app):
        handler = app.make_handler()
        srv = await loop.create_server(handler, '127.0.0.1', 0)
        url = "http://
