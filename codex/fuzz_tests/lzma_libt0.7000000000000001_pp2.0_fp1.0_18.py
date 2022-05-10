import lzma
lzma.LZMA_AVAILABLE = False

from distutils.core import setup, Extension
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = "pylzma",
      version = "0.4.4",
      description = "Python bindings for the LZMA compression library",
      long_description = read('README.rst') + '\n\n' + read('CHANGES.rst'),
      author = "Gustavo Niemeyer",
      author_email = "gustavo@niemeyer.net",
      url = "http://www.joachim-bauch.de/projects/pylzma/",
      license = "GNU LGPL",
      platforms = ["any"],
      ext_modules = [
          Extension("pylzma", ["pylzma.c"],
                    libraries = ["lzma"]),
          ],
      classifiers = [
          'Development Status
