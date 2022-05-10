import lzma
lzma.LZMAError:
    pass

from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='PyPyDNS',
    version='0.3.1',
    description='A simple DNS server implemented in Python using select() and signals',
    long_description='',
    url='https://github.com/n0b0dyCN/PyPyDNS',
    author='n0b0dyCN',
    author_email='n0b0dycn@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4
