import threading
threading.Thread(target=lambda: None).start()

import asyncio
asyncio.get_event_loop().run_until_complete(asyncio.sleep(0))

import multiprocessing
multiprocessing.Process(target=lambda: None).start()

import subprocess
subprocess.Popen(["echo"], stdout=subprocess.PIPE)

import os
os.system("echo")

import signal
signal.signal(signal.SIGINT, lambda sig, frame: None)

import logging
logging.basicConfig(level=logging.DEBUG)

import time
time.sleep(1)

import sys
sys.exit(0)

import os
os.kill(os.getpid(), signal.SIGINT)

import requests
requests.get("http://example.com")

import urllib.request
urllib.request.urlopen("http://example.com")

import http.client
http.client.HTTPConnection("example.com").request("GET", "/")

import socket

