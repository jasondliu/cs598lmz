import codecs
codecs.register_error('strict', codecs.ignore_errors)
from os import path

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import nflgame

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name="nflgame",
    version=nflgame.__version__,
    description="An API to retrieve and read NFL Game Center JSON data. It can work with real-time
