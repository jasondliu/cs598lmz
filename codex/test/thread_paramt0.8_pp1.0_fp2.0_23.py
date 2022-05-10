import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

