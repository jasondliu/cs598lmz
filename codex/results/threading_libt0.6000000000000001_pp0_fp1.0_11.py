import threading
threading.stack_size(8388608)

import os
import sys
import time
import uuid
import json
import traceback
import base64
import datetime
import subprocess
import logging
import logging.handlers
import argparse
import urllib
import urllib2

from multiprocessing import Queue
from subprocess import Popen, PIPE
from threading import Thread

from flask import Flask, request, jsonify, abort, send_from_directory
from flask_cors import CORS

from redis import StrictRedis
from redis.exceptions import ConnectionError

from werkzeug.utils import secure_filename

import cv2
import numpy as np

from custom_utils import *

from darkflow.net.build import TFNet

# Import Openpose (Windows/Ubuntu/OSX)
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path + "/openpose/"
try:
    # Windows Import
    if platform == "win32":

