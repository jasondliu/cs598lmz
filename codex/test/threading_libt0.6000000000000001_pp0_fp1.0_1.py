import threading
threading.stack_size(8*1024*1024)

import os
import json
import sys
import traceback
import logging
import time
import datetime
import copy
import pprint
import operator
import re
import urllib

from collections import OrderedDict
from collections import Counter

from jinja2 import Environment, FileSystemLoader

from pymongo import MongoClient
from bson.objectid import ObjectId

from flask import Flask, render_template, url_for, request, Response, redirect, make_response, make_response, send_from_directory
from flask import jsonify
from flask import g
from flask import copy_current_request_context
from flask import session

from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

from bson.objectid import ObjectId
from bson.json_util import dumps

from datetime import datetime
from datetime import date
from datetime import timedelta

from dateutil.relativedelta import relat
