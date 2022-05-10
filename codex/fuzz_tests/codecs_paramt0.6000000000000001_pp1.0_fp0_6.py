import codecs
codecs.register_error('strict', codecs.ignore_errors)

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'requests>=2.13',
    'requests-cache>=0.4.13',
    'beautifulsoup4>=4.5.0',
    'pymongo>=3.3.0',
]

setup(
    name='deepinjector',
    version='0.1.0',
    description="Deep learning data injector",
    long_description=readme + '\n\n' + history,
    author="Juan Manuel Schillaci",
    author_email='jmschillaci@gmail.com',
    url='
