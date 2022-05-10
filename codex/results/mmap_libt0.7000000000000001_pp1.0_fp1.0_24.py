import mmap
import os,sys
import re
import shutil
import subprocess
import tempfile
import time
import uuid
import traceback
from datetime import datetime
import socket
import struct
from config import Config

logger = logging.getLogger('swift.obj.updater')

def exec_cmd(cmd, stdin=None, stderr=None, stdout=None):
    """
    Run the given command in the given working directory,
    with the given stdin, stdout and stderr file descriptors.
    """
    logger.info('executing: ' + cmd)
    start = time.time()
    exitcode = subprocess.call(cmd, stdin=stdin, stdout=stdout, stderr=stderr)
    end = time.time()
    logger.info('execution took %.2f seconds and ended with exit code %s' % (
        end-start, exitcode))
    return exitcode


def get_partition_path(config, account, container=None, object=None):
    """

