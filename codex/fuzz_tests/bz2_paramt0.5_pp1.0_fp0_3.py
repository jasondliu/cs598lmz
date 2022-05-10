from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = decompress

# Needed to avoid a bug in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name='django-waffle',
    version='0.2.2',
    description='A feature flipper for Django.',
    long_description=open('README.rst').read(),
    author='James Socol',
    author_email='me@jamessocol.com',
    url='http://github.com/jsocol/django-waffle',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,  # because we're including media that Django needs
    install_requires=[
        'django>=1.3',
        'pytz>=2011b',
    ],
    tests_require=[
        'django-nose',
        '
