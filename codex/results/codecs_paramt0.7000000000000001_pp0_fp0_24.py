import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
package = os.path.join(here, 'src', 'behave')
version = os.path.join(package, 'version.py')

requirements = os.path.join(here, 'requirements.txt')
with open(requirements, 'r') as f:
    required = f.read().splitlines()

with codecs.open(version, encoding='utf-8') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup
