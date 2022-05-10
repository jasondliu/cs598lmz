import codecs
codecs.register_error('strict', codecs.ignore_errors)

from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-pagination-bootstrap',
    version='1.2.0',
    description='Bootstrap pagination for Django',
    long_description=long_description,
    url='https://github.com/jamespacileo/django-pagination-bootstrap',
    author='James Pacileo',
    author_email='jamespacileo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python
