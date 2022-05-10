import select
import socket
import time

from pgoapi.utilities import f2i, get_pos_by_name
from threading import Thread, Lock
from Queue import Queue, Empty
from s2sphere import Cell, CellId, LatLng

from . import config
from .models import parse_map


TIMESTAMP = '\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000'

REQ_SLEEP = 0.5
REQ_TIMEOUT = 15

TRAVERSAL_PAYLOAD = '05daf51635c82611d1aac95c0b051d3ec088a930' + TIMESTAMP

REQ_SESSION_NEW = '\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000
