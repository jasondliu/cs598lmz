import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name='django-debug-toolbar',
    version='0.9.4',
    description='A configurable set of panels that display various debug information about the current request/response.',
    long_description=open('README.rst').read(),
    author='Rob Hudson',
    author_email='rob@cogit8.org',
    url='http://github.com/django-debug-toolbar/django-debug-toolbar',
    packages=find_packages(exclude=('tests.*', 'tests', 'example')),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Aud
