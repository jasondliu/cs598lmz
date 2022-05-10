import mmap
import os
import random
import shutil
import socket
import subprocess
import sys
import time
import traceback
import yaml

from collections import defaultdict
from contextlib import contextmanager
from functools import wraps
from glob import glob
from itertools import product
from re import compile as re_compile
from socket import getfqdn

from charmhelpers.core import (
    host,
    hookenv,
    unitdata,
)

from charmhelpers.core.hookenv import (
    cached,
    config,
    log,
    relation_get,
    relation_ids,
    relation_set,
    relation_type,
    unit_get,
    unit_private_ip,
)

from charmhelpers.core.host import (
    lsb_release,
    mkdir,
    service,
    service_running,
    service_restart,
    service_start,
    service_stop,
    write_file,
)

from charmhelpers.core.strutils import (
    bool_from_string,
