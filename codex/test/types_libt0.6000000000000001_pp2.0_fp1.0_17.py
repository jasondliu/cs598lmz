import types
types.ModuleType.__dict__['__getattr__'] = types.ModuleType.__getattribute__
types.ModuleType.__dict__['__setattr__'] = types.ModuleType.__setattr__

import os
import sys
import uuid
import marshal
import random
import base64
import tempfile
import zipfile
import platform

from ctypes import *

from Crypto.Cipher import ARC4

from bottle import Bottle, route, run, request, response, abort
from bottle import static_file, redirect, error, HTTPResponse
from bottle import jinja2_template as template

from config import get_config

app = Bottle()

# add the config to the app
app.config = get_config()

# add the database to the app
app.db = app.config['db']

# add the crypto to the app
app.crypto = app.config['crypto']

# add the libs to the app
app.libs = app.config['libs']

# add the templates to the app
app.templates = app
