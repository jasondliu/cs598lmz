import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re

from . import util
from . import config
from . import log
from . import error
from . import process
from . import shell
from . import git

from .util import *
from .config import *
from .log import *
from .error import *
from .process import *
from .shell import *
from .git import *

def _get_tag(tag):
    try:
        return git.tag_list()[tag]
    except KeyError:
        raise error.Error('tag "%s" not found' % tag)

def _get_branch(branch):
    try:
        return git.branch_list()[branch]
    except KeyError:
        raise error.Error('branch "%s" not found' % branch)

def _get_ref(ref):
    try:
        return git.ref_list()[ref]
    except KeyError:
        raise error.Error('ref "%s" not found' % ref)

def _
