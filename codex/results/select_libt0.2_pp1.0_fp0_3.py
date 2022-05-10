import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import util

try:
    import ssl
except ImportError:
    ssl = None

try:
    import OpenSSL
except ImportError:
    OpenSSL = None

try:
    import cryptography
except ImportError:
    cryptography = None

try:
    import idna
except ImportError:
    idna = None

try:
    import certifi
except ImportError:
    certifi = None

try:
    import urllib3
except ImportError:
    urllib3 = None

try:
    import requests
except ImportError:
    requests = None

try:
    import aiohttp
except ImportError:
    aiohttp = None

try:
    import tornado
except ImportError:
    tornado = None

try:
    import asyncio
except ImportError:
    asyncio = None

try:
    import websockets
except ImportError:
    websockets = None

try:
    import
