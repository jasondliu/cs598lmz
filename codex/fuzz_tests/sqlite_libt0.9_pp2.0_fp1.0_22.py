import ctypes
import ctypes.util
import threading
import sqlite3
import json
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")

logger = logging.getLogger("webserver")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("/tmp/webserver.log")
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

if not os.path.isdir("/tmp/yubiserver/"):
    os.mkdir("/tmp/yubiserver/")

conn = sqlite3.connect("/tmp/yub
