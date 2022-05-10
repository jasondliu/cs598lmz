import signal
signal.signal(signal.SIGINT, signal.default_int_handler)

from core.logger import Logger
from core import config
from core import *
from core.plugin_system import PluginSystem, Plugin
from core.utils import Utils
from core.exceptions import *
from core.config import Config
from core.plugins import Plugins

from core.commands.context import Context

from data.database import Database
from data.user import User

from core.mq import *

import uuid

from flask import Flask, g, request, jsonify
from flask.ext.restful import Resource, Api, abort, reqparse, fields, marshal
from flask.ext.cors import CORS

import atexit

logger = Logger(__name__)

plugins = PluginSystem()

class Auth(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, required = True, help = 'No username provided', location = 'json')
