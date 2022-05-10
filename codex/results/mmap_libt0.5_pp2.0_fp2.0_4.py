import mmap
import re
import sys
import time

from collections import namedtuple
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from os import path
from os import listdir
from os import stat
from os import remove
from os import rename
from os import makedirs
from os import strerror
from os import O_CREAT
from os import O_RDWR
from os import O_APPEND
from os import O_NONBLOCK
from os import O_NOCTTY
from os import O_SYNC
from os import O_TRUNC
from os import O_RDONLY
from os import O_WRONLY
from os import SEEK_SET
from os import SEEK_CUR
from os import SEEK_END
from os import R_OK
from os import W_OK
from os import X_OK
from os import F_OK
from os import environ
from os import pathsep
from os import devnull
from os import fdopen
from os import getcwd
from os import getcwdb
from os import ch
