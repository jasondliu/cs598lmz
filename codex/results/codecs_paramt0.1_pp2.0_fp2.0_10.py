import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import time
import json
import requests
import argparse
import logging
import logging.config
import logging.handlers
import traceback
import subprocess
import threading
import multiprocessing
import Queue
import signal
import shutil
import tempfile
import zipfile
import tarfile
import glob
import hashlib
import base64
import random
import string
import copy
import math
import datetime
import platform
import pprint
import cPickle as pickle
import ConfigParser
import xml.etree.ElementTree as ET

from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
from collections import Counter
from collections import deque
from collections import Iterable
from collections import Mapping
from collections import Sequence
from collections import Set
from collections import Sized
from collections import Container
from collections import Hashable
from collections import Callable
from collections import Generator
from collections import Iterator
from collections import ByteString
from collections import TextString
from collections import ItemsView
from collections
