import gc, weakref
import cPickle as pickle
import cStringIO as StringIO
import csv
import logging
import math
import os
import re
import sys
import time
import traceback
import urllib
import urlparse
import itertools
import operator
import pkg_resources
import collections

from collections import deque
from contextlib import closing
from copy import copy, deepcopy
from datetime import datetime, date, time as dtime
from decimal import Decimal
from functools import partial, wraps
from inspect import isclass, isgenerator, cleandoc
from itertools import chain
from operator import itemgetter, attrgetter
from pprint import pformat
from re import compile
from urlparse import urljoin
from uuid import uuid4

from lxml import etree

from mongoengine import signals, document, queryset
from mongoengine.base import get_document
from mongoengine.connection import get_connection, DEFAULT_CONNECTION_NAME
from mongoengine.context_managers import switch_db, switch_collection
from mongoengine.
