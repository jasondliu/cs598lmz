import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from collections import defaultdict
from glob import glob
from multiprocessing import Pool
from os.path import basename, dirname, join, exists, isdir, isfile, realpath, splitext
from urllib.parse import urlparse

import requests
