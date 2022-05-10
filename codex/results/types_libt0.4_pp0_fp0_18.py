import types
types.ModuleType.__init__ = types.ModuleType.__new__

import sys, os, re, time, datetime, urllib, urllib2, urlparse, cookielib, socket, json, random, string, base64, hashlib, gzip, StringIO, httplib, HTMLParser, copy, inspect, threading, Queue, xbmc, xbmcgui, xbmcplugin, xbmcaddon, xbmcvfs, xbmcgui, xbmcaddon, xbmc
from urllib2 import HTTPError, URLError
from urllib import quote, unquote, quote_plus, unquote_plus, urlencode
from urlparse import parse_qsl

try:
    from sqlite3 import dbapi2 as sqlite
    print "Loading sqlite3 as DB engine"
except:
    from pysqlite2 import dbapi2 as sqlite
    print "Loading pysqlite2 as DB engine"

try:
    import StorageServer
except:
    import storageserverdummy as StorageServer

# global variables
