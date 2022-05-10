import mmap
import os
import re
import sys
import tempfile
import time
import zipfile
from io import BytesIO
from os.path import basename, dirname, exists, join, normpath, splitext
from shutil import copyfileobj
from subprocess import Popen, PIPE
from threading import Thread
from zipfile import ZipFile

