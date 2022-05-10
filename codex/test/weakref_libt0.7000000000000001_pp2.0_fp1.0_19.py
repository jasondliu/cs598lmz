import weakref
import copy
import pprint
import types
import threading
import time
import random
import logging
import pickle
import sys
import traceback
import signal
import os
import re
import ssl
import Queue

from uuid import uuid4

from bson import json_util

from flask import Flask, request, abort, Response, render_template_string, make_response, redirect, jsonify
from flask_compress import Compress

from flask_sockets import Sockets

from flask.ext.cors import CORS

import gevent
import gevent.monkey
import gevent.wsgi
import gevent.server
import gevent.ssl

monkey_patch = gevent.monkey.patch_all(aggressive=True)

import pymongo

from pymongo import MongoClient
from pymongo import ReadPreference
from pymongo.errors import AutoReconnect
from bson.objectid import ObjectId

from pymongo_hadoop import BSONMapper

from bson.codec_options import CodecOptions

