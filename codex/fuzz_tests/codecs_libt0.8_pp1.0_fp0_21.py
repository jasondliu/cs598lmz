import codecs
codecs.register(GS1Codec.search_function)

import re
from setuptools import setup, find_packages
from pip.req import parse_requirements

from gs1 import version


def read_file(path, encoding='utf-8'):
    with open(path, encoding=encoding) as f:
        return f.read()


def get_requirements(filename):
    install_reqs = parse_requirements(filename, session='hack')
    return [str(ir.req) for ir in install_reqs]


long_description = read_file('README.rst')

setup(
    author='Hiroaki Kawai',
    author_email='hiroaki.kawai@gmail.com',
    description='Validation and generation tools for various GS1 keys',
    name='gs1',
    url='https://github.com/hkwi/python-gs1',
    version=version,
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
    long_description=long_
