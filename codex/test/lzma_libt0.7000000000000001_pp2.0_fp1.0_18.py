import lzma
lzma.LZMA_AVAILABLE = False

from distutils.core import setup, Extension
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

