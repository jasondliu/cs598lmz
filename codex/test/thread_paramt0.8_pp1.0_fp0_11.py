import sys, threading
threading.Thread(target=lambda: sys.stdout.write("VARIABLE = 0\n")).start()
threading.Thread(target=lambda: sys.stdout.write("VARIABLE = 1\n")).start()

# using a global variable to store the name of the executable
executable = sys.argv[0]
import os
# using os.path.basename to extract the filename
executable = os.path.basename(executable)

from os import getenv
from os.path import join
from subprocess import run
from sys import platform

from Cython.Build import cythonize
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


