import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(name='quart',
      version='0.1.0',
      description='A microframework based on Asyncio.',
      long_description=readme,
      author='Kenneth Reitz',
      author_email='me@kennethreitz.org',
      url='https://github.com/kennethreitz/quart',
      packages=['quart'],
      entry_points={
          'console_scripts': [
              'quart = quart.cli:cli'
          ]
      },
      install_requires=[
        'Werkzeug',
        'itsdangerous'
      ],
      classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI
