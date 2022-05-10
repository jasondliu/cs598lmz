import lzma
lzma.LZMAError

import re
import os
import sys
import time
import shutil
import logging
import tempfile
import subprocess
import multiprocessing
import multiprocessing.pool
import multiprocessing.dummy

import pkg_resources

import pkgcore.ebuild
import pkgcore.restrictions
import pkgcore.util.commandline
import pkgcore.util.parserestrict
import pkgcore.util.packages
import pkgcore.util.currying
import pkgcore.util.text

from snakeoil.demandload import demandload
from snakeoil.osutils import pjoin, listdir_files, listdir_dirs
from snakeoil.fileutils import readfile, write_file, AtomicWriteFile
from snakeoil.process import CommandNotFound, Command
from snakeoil.currying import post_curry
from snakeoil.lists import iflatten_instance
from snakeoil.klass import jit_attr
from snakeoil.mappings import ImmutableDict
from snakeoil.sequences import iflatten_instance

