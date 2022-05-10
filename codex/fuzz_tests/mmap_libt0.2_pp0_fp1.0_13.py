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

from buildbot.process.properties import Properties
from buildbot.steps.shell import ShellCommand
from buildbot.steps.source import Mercurial
from buildbot.steps.transfer import FileUpload
from buildbot.status.builder import SUCCESS, WARNINGS, FAILURE, SKIPPED, EXCEPTION

from buildbotcustom.common import get_hg_revision_branch, get_hg_revision_tag, \
                                  get_hg_revision_changeset, get_hg_revision_pushlog_id, \
                                  get_hg_revision_pushdate, get_hg_revision_pushtime, \
                                  get_hg_revision_author, get_hg_revision_desc, \
                                  get_hg_revision_bookmarks, get_hg_
