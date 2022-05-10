import mmap
import os
import re
import shutil
import subprocess
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import uuid
import xml.sax.saxutils
import zipfile

from optparse import OptionParser
from os import path
from pprint import pprint
from random import randint
from subprocess import Popen, PIPE, STDOUT
from sys import exit, platform
from threading import Thread
from time import sleep
from xml.dom.minidom import parse

from buildbot.status import builder
from buildbot.status.results import SUCCESS, WARNINGS, FAILURE, EXCEPTION, RETRY
from buildbot.steps.source import SVN
from buildbot.steps.shell import Compile, ShellCommand
from buildbot.steps.shell import WarningCountingShellCommand
from buildbot.steps.transfer import FileUpload
from buildbot.process.properties import WithProperties
from buildbot.process.properties import Properties
from buildbot.process.results import FAILURE, SUCCESS
from buildbot.
