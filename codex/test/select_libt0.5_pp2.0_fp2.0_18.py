import select
import socket
import sys
import threading
import time

from gi.repository import GObject

from pychess.System import uistuff
from pychess.System.Log import log
from pychess.System.prefix import addDataPrefix
