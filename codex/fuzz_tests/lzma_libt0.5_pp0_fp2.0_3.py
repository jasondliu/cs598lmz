import lzma
lzma.open

# -*- coding: utf-8 -*-
#
# File: __init__.py
#
# Copyright (c) 2017 by Imio.be
#
# GNU General Public License (GPL)
#

__author__ = """Gauthier Bastien <g.bastien@imio.be>"""
__docformat__ = 'plaintext'

# The following iterates over all the packages defining a __version__ attribute
# and if needed replaces it by a dynamic value which takes into account
# svn properties.
# Adapted from zest.releaser.
import os
import subprocess
import sys
import re

# Do not use pkg_resources for this, as it is not yet installed when this file
# is read.
def get_svn_revision(path):
    revision = None
    entries_path = '%s/.svn/entries' % path

    if os.path.exists(entries_path):
        entries = open(entries_path, 'r').read()
        # Versions >= 7
