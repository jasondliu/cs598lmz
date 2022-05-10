import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import uuid

import common
import edify_generator

OPTIONS = common.OPTIONS


def Run(cmd, stdin=None, stdout=None, stderr=None, shell=False):
  """Run a command and return its returncode, stdout, and stderr."""
  if OPTIONS.verbose:
    print "Running", cmd
  if stdin:
    stdin = open(stdin, "rb")
  if stdout:
    stdout = open(stdout, "wb")
  if stderr:
    stderr = open(stderr, "wb")
  p = subprocess.Popen(cmd, stdin=stdin, stdout=stdout, stderr=stderr,
                       shell=shell)
  p.communicate()
  return p.returncode, stdout, stderr


def AddToZip(input_zip, output_zip, input_path
