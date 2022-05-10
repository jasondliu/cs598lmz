import mmap
import os
import sys

from . import util
from . import version
from . import xattr
from . import xattrnames
from . import xattrvalue

# pylint: disable=too-many-instance-attributes
class File(object):
  """
  A file on the filesystem.
  """

  def __init__(self, path):
    self.path = path
    self.stat = os.stat(path)
    self.xattrs = xattr.listxattr(path)
    self.xattr_values = {}

    # If the file is a symlink, we need to store the target of the symlink,
    # because we will be hashing the target and not the symlink.
    if os.path.islink(path):
      self.target = os.readlink(path)
    else:
      self.target = None

    # If the file is a directory, we need to store the names of all the
    # files inside the directory, because we will be hashing the names of
    # the files and not the contents of the files
