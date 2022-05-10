import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import os
import sys
import time
import getopt
import subprocess
import shlex
import shutil
import platform
import re

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))

if not LOCAL_PATH.endswith("/"): LOCAL_PATH += "/"

sys.path.append(LOCAL_PATH + "tools/ModisTool/")

from credentials import credentials
import modis_tool

GIT_CLIENT = "git"

# Update cvs projects
def execute_git(command, dir_name, short=False):
    cmd = shlex.split(command)
    p = subprocess.Popen(
        cmd, cwd=dir_name, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, close_fds=True)
    return p.communicate()[0]


