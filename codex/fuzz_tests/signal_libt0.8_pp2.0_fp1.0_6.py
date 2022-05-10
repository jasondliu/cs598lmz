import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
from setuptools import setup

from g2p.g2p_server import __version__, __author__, __email__

setup(
    name='g2p-server',
    version=__version__,
    description='g2p-server is a Grapheme-to-Phoneme server',
    long_description=open('README.rst').read(),
    author=__author__,
    author_email=__email__,
    url='https://github.com/Kyubyong/g2p-server/',
    packages=['g2p'],
    install_requires=['falcon', 'gunicorn', 'tqdm'],
    keywords='g2p, grapheme-to-phoneme server',
    package_data={'g2p': ['*.pickle']},
    license='MIT'
)
