import gc, weakref
import json
import logging
import os
import re
import sys
import time
import traceback
import types

try:
    import socketio
    import socketio.client
    import socketio.exceptions
except ImportError:
    socketio = None

try:
    import websockets
except ImportError:
    websockets = None

try:
    import aiohttp
except ImportError:
    aiohttp = None

