import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'jdcal',
]

requires = []

setup(
    name='jdcal',
    version='1.0',
    description='Julian dates from proleptic Gregorian and Julian calendars.',
    long_description=open('README.rst').read(),
    author='Charles R Harris',
    author_email='charlesr.harris@gmail.com',
    url='https://github.com/phn/jdcal',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'jdcal': 'jdcal'},
    include_package_data=True,
    install_requires=requires,
    license=open('
