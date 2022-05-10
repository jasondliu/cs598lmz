import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import time
import os
import re
import subprocess
import traceback
import string
import threading
import Queue
import cPickle
import gzip
import shutil
import socket
import cStringIO
import tempfile
import urllib
import urllib2
import urlparse
import gtk
import gtk.gdk
import gobject
import pango
import webkit
import jswebkit
import cookielib

from idlelib.TreeWidget import TreeItem, TreeStore

from idlelib import Browser

import pygtk
pygtk.require('2.0')

from idlelib import SearchDialog

import idleconf
import PathBrowser
import RemoteDebugger
import Debugger
import Debugger.debugger
import Debugger.debugger_rpc
import Debugger.debugger_thread
import Debugger.debugger_utils
import Debugger.debugger_vars
import Debugger.debugger_stepping
import Debugger.debugger_trace
import Debugger
