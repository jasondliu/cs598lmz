import _struct
import array
import pickle
import os
import os.path
import glob
import string
import re
import time
import copy
import types
import math

# Python 2.4 or later
try:
    set
except NameError:
    from sets import Set as set

# Python 2.4 or later
try:
    sorted
except NameError:
    def sorted(l):
        l = list(l)
        l.sort()
        return l

def _get_version_string():
    import sys
    try:
        import svn.core
        import svn.repos
    except ImportError:
        if not hasattr(sys, "frozen"):
            return " (from source)"
        return ""
    try:
        repo = svn.repos.open(".")
        rev = svn.core.svn_opt_revision_t()
        rev.kind = svn.core.svn_opt_revision_head
        root = repo.fs_root(rev)
        id = root.node_id("./")
