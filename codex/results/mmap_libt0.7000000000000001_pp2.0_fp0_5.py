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
    def __init__(self, project, version,
                 builder='dev',
                 build_type='Release',
                 build_dir=None,
                 arch='x86_64',
                 config=None,
                 out_dir=None,
                 build_number=None,
                 incremental=False,
                 platform='linux',
                 copy_build=True,
                 build_image=None,
                 build_script=None,
                 build_script_args=None,
                 build_script_env=None):
        """
        Initialize a build

        :param project:             Project name
        :param version:             Project version
        :param builder:            
