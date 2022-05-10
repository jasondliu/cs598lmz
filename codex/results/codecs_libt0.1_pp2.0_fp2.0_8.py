import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import sys
import json
import requests
import datetime
import time
import threading
import queue
import logging
import logging.handlers
import traceback
import subprocess
import re
import math
import random
import string
import base64
import hashlib
import hmac
import urllib
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import http.client
import mimetypes
import ssl
import socket
import select
import struct
import copy
import shutil
import platform
import pprint
import glob
import uuid
import psutil
import signal
import pwd
import grp
import getpass
import pty

