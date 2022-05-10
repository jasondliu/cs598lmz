import mmap
import os
import time
import shutil
import re
import tarfile
import tempfile
import subprocess
import sys
import glob

if sys.version_info >= (3,4):
    import configparser
else:
    import ConfigParser as configparser

class BuildError(Exception):
    pass

class Build(object):
    """
    Build object represents a build of a specific version of the project
    """
