import gc, weakref
import re, os, sys
import time
import threading
import traceback
import logging
import logging.handlers
import datetime
import pytz
import Queue
import types
import inspect
import json
import pkg_resources
import copy
import math

from collections import defaultdict
from functools import wraps

from twisted.internet import reactor, defer
from twisted.python import log
from twisted.python.failure import Failure

from opennsa import nsa, error, config, scheduler
from opennsa.topology import nml, nmlstatemodel, nmlformat
from opennsa.protocols.nsi2 import helper, header, error as nsaerr
from opennsa.protocols.nsi2.bindings import bindings

from opennsa.backends import common, agnostic, simple, backend
from opennsa.backends.common import scheduler as backendscheduler

from opennsa import ietf, subrequester



logger = logging.getLogger(__name__)

CONTENT_TYPE_NSI
