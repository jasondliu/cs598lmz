import types
types.FileType = file
import sys
import os
import re
import imp
import time
import traceback
import threading
import inspect
import gc
import __builtin__

from StringIO import StringIO
from pprint import pprint
from collections import defaultdict

from twisted.python import log
from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList, inlineCallbacks
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.wsgi import WSGIResource
from twisted.web.http import Request, HTTPChannel
from twisted.web.error import NoResource

from flask import Flask, Response
from flask.ext.restful import Api, Resource, reqparse

from . import config
from . import utils
from . import security
from . import __version__


def _log(msg, *args):
    if args:
        msg = msg % args

