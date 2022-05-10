import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import zipfile

from optparse import OptionParser

from buildbot.steps.source import SVN
from buildbot.steps.shell import ShellCommand
from buildbot.steps.shell import SetPropertyFromCommand
from buildbot.steps.shell import WarningCountingShellCommand
from buildbot.process.properties import WithProperties
from buildbot.process.buildstep import LogLineObserver
from buildbot.process.buildstep import SUCCESS, FAILURE, WARNINGS, SKIPPED
from buildbot.status.builder import SUCCESS, WARNINGS, FAILURE, SKIPPED, EXCEPTION
from buildbot.status.results import Results
from buildbot.status.results import SUCCESS, WARNINGS, FAILURE, SKIPPED, EXCEPTION
from buildbot.status.results import worst_status
from buildbot.status.builder import SUCCESS, WARNINGS, FAILURE, SKIPPED,
