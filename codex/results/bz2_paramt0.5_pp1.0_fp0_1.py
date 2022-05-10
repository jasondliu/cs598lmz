from bz2 import BZ2Decompressor
BZ2Decompressor()

import re
import os
import sys
import time
import json
import requests
import getpass
import datetime
import traceback
import subprocess

from pyquery import PyQuery as pq

# *****************************************************************************
#                                                                             *
# *****************************************************************************

class RequestError(Exception):
    pass

# *****************************************************************************
#                                                                             *
# *****************************************************************************

class Request:
    def __init__(self, url, post=None, **kwargs):
        self.url = url
        self.post = post
        self.kwargs = kwargs
    def __repr__(self):
        return 'Request(%r, %r, %r)' % (self.url, self.post, self.kwargs)
    def __str__(self):
        return repr(self)

# *****************************************************************************
#                                                                             *
# *****************************************************************************

class Request_Manager:
    def __init__(self, session, requests=None, **kwargs):
        self.session
