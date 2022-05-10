import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from pip._internal.main import main

from flask_pdfkit import PDFKit
from flask_socketio import SocketIO
import flask
from flask_compress import Compress
from flask import Flask
from datetime import datetime
import subprocess
import sys
import time
import os
import shutil
import traceback
import tempfile
import threading
from PIL import Image
from io import BytesIO
import numpy as np
from tinytag import TinyTag
import requests
from bs4 import BeautifulSoup
from ffmpy import FFmpeg
from math import ceil
import re
from urllib.request import urlretrieve
from werkzeug.utils import secure_filename
from flask_mail import Message, Mail
from concurrent.futures import ThreadPoolExecutor
import asyncio
import concurrent.futures
from concurrent import futures
from threading import Thread
from multiprocessing import Process
from random import randint as rand
from copy import copy as c
