import mmap
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time

from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.sdist import sdist
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from setuptools.command.build_scripts import build_scripts
from setuptools.command.bdist_egg import bdist_egg
from setuptools.command.bdist_rpm import bdist_rpm

# We use a custom build_ext command to make sure that
# distutils.sysconfig.get_config_var('LDSHARED') is always set to the
# correct value, otherwise it will only be set if we actually build
# any extensions.
class _build_ext(build_ext):

    def finalize_options(self):
        build_ext.finalize_options(self
