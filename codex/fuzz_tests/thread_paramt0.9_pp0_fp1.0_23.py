import sys, threading
threading.Thread(target=lambda: sys.initialize()).start()

from proxy import MirrorServer, MirrorClient
from datetime import datetime
from time import time, sleep
import os.path, re, socket, json, shutil, threading, cgi, logging
from multiprocessing import Process, Pipe
from . import lib
from .lib import get_logger
import aiohttp, asyncio, io, pathlib, sys, logging, atexit

at_exit = []
def _at_exit():
    for task in at_exit:
        try: task()
        except: pass
atexit.register(_at_exit)

def get_logs_path(base_path):
    root_logs_path = os.path.join(base_path, 'logs')
    pathlib.Path(root_logs_path).mkdir(exist_ok=True)
    port = int(os.environ.get('PORT', 80))
    return os.path.join(root_logs_path, 'app-{}.log'.format(port))

class CustomHandler(logging.
