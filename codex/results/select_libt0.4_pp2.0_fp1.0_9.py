import select
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from util import *

#==============================================================================
class Stream:
    #--------------------------------------------------------------------------
    def __init__(self, url, options):
        self.url = url
        self.options = options
        self.buffer_size = options.buffer_size
        self.buffer = ''
        self.buffer_start = 0
        self.buffer_end = 0
        self.buffer_len = 0
        self.buffer_duration = 0
        self.buffer_duration_target = options.buffer_duration
        self.buffer_duration_min = options.buffer_duration_min
        self.buffer_duration_max = options.buffer_duration_max
        self.buffer_duration_grow = options.buffer_duration_grow
        self.buffer_duration_shrink = options.buffer_duration_shrink
        self.buffer_duration_last_grow = 0
        self.buffer_duration_last_shrink = 0
        self.buffer_duration_last_adjust = 0

