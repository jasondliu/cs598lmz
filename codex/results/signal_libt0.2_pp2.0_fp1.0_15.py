import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import subprocess
import re
import time
import datetime
import shutil
import json
import urllib
import urllib2
import socket
import logging
import argparse
import traceback
import threading
import Queue
import ConfigParser
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstPbutils', '1.0')
gi.require_version('GstApp', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import G
