import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from bs4.element import Comment
from bs4.element import NavigableString
from bs4.element import Tag
from bs4.element import CData

from collections import defaultdict
from collections import deque
from collections import namedtuple

from datetime import datetime

from itertools import chain
from itertools import izip
from itertools import product
from itertools import tee

from multiprocessing import Process
from multiprocessing import Queue

from Queue import Empty

from random import randint
from random import shuffle

from re import compile
from re import findall
from re import match
from re import search
from re import sub

from socket import error as SocketError

from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punct
