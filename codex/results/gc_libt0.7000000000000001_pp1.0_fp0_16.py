import gc, weakref, inspect

from types import MethodType, FunctionType

import sys, os, os.path, shutil, re, hashlib, codecs, base64, math, glob

from struct import unpack

from xml.sax.saxutils import escape

from traceback import print_exc, print_stack

from heapq import nsmallest, nlargest

from functools import partial

from datetime import datetime, timedelta

from random import choice, sample, randint, random, shuffle

from urlparse import urlparse, urlunparse

from urllib import quote_plus, unquote_plus

from urllib2 import urlopen, URLError, HTTPError

from StringIO import StringIO

from collections import defaultdict

from itertools import count

from operator import itemgetter, attrgetter, methodcaller

from contextlib import contextmanager

from uuid import uuid1, uuid4

import re

import time, calendar

import json, csv

import md5, sha

import sqlite
