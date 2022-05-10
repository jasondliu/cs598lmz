import select
from errno import EINTR
from threading import Thread
from functools import partial
from StringIO import StringIO
import logging

from HTTPUtils import *

logger = logging.getLogger(__name__)


