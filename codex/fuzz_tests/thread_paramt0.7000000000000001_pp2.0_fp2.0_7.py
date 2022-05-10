import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;31m')).start()
#

from time import time as _time, sleep as _sleep
from random import random as _random
from json import dumps as _json_dumps
from copy import deepcopy as _deepcopy
from traceback import format_exc as _format_exc
from numbers import Number as _Number
from ast import literal_eval as _literal_eval
from datetime import datetime as _datetime
from os.path import join as _path_join
from os.path import exists as _path_exists
from os import remove as _os_remove, makedirs as _os_makedirs
from os import mkdir as _os_mkdir
from shutil import copy as _shutil_copy
from shutil import copytree as _shutil_copytree

from flask import Flask, Response
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask_socketio import SocketIO, emit

from werkzeug.utils import secure_filename
from werkzeug.ex
