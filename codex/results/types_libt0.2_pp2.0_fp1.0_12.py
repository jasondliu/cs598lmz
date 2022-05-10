import types
types.MethodType(lambda self: None, None, None)

# This is a workaround for http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name='django-haystack',
    version='2.0.0-beta',
    description='Pluggable search for Django.',
    long_description=open('README.rst').read(),
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    url='http://haystacksearch.org/',
    packages=find_packages(exclude=['example_project', 'example_project.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language ::
