import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import glob
import re
import subprocess
import shutil
import time
import urllib2
import urlparse
import zlib
import json
import tempfile
import pprint

from optparse import OptionParser

import sgmllib

import git
import git.util
import git.remote
import git.exc
import git.config

import gitutil
import git_version

from util import *

class VersionControlSystem(object):
    def __init__(self, name, get_url_command, get_url_regex, get_revision_command, get_revision_regex, clone_command, clone_regex, update_command, update_regex, push_command, push_regex, push_branch_command, push_branch_regex, get_files_command, get_files_regex, pull_command, pull_regex, pull_branch_command, pull_branch_regex):
        self.name = name
        self.get_url
