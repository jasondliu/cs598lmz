import codecs
codecs.register_error('strict', codecs.ignore_errors)

from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-dynamic-preferences',
    version='1.7.1',
    description='Django Dynamic Preferences is a Django app that allows users to manage their own settings.',
    long_description=long_description,
    url='https://github.com/jazzband/django-dynamic-preferences',
    author='Alexandre Andrieux',
    author_email='contact@alexandre.andrieux.me',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework ::
