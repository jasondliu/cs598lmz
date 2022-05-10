import codecs
codecs.register_error('strict', codecs.ignore_errors)

from ircbot import SingleServerIRCBot
from irclib import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr

from twisted.internet import reactor, protocol, ssl
from twisted.words.protocols import irc
from twisted.internet.task import LoopingCall
from twisted.python import log

from threading import Thread
from random import randint

from datetime import datetime

from os import environ

from collections import defaultdict

import sys
import traceback
import time
import re

from config import *

from plugins import *

import sqlite3

import json

from collections import defaultdict

import requests

from requests.exceptions import ConnectionError

from lxml import html

import feedparser

import urllib2

from bs4 import BeautifulSoup

from time import gmtime, strftime

from lxml import etree

import urllib

import socket

