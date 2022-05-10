import lzma
lzma.LZMA_FORMAT_AUTO = 0
lzma.LZMA_FORMAT_XZ = 1
lzma.LZMA_FORMAT_ALONE = 2
lzma.LZMA_FORMAT_RAW = 3

import os
import sys
import time
import re
import subprocess
import shutil
import tempfile
import logging
import argparse
import multiprocessing
import threading
import queue
import copy
import collections
import functools
import itertools
import contextlib
import traceback
import textwrap
import pprint
import pickle
import struct
import binascii
import hashlib
import platform
import json
import io
import zlib
import base64
import socket
import urllib.request
import urllib.parse
import urllib.error
import http.server
import socketserver
import http.client
import html.parser
import email.parser
import email.policy
import email.utils
import email.mime.text
import email.mime.multipart
import email.mime.application
