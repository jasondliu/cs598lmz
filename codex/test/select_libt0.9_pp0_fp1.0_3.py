import selectors
import socketserver
import re
import asyncio
import aiohttp
import aiofiles
from aiohttp import web

from controllers.models import Users
from utils.tools import getRandom

# 解决报错：asyncio: debug mode is not supported on Windows
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Servers(socketserver.ThreadingTCPServer):
    """Serves a POST connection,
    reads the POST data for the specified form and writes
    the desired output to the socket."""

    request_queue_size = 50  # 排队数
    allow_reuse_address = 1  # 允许地址重用
    timeout = 10  # 设置超时
    address_family = socket.AF_INET
    # daemon_threads = 1

