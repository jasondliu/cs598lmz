import codecs
codecs.register_error('strict', codecs.ignore_errors)

from setuptools import setup, find_packages

setup(
    name='pytest-cov',
    description='pytest plugin for measuring coverage',
    long_description=open('README.rst').read(),
    version='2.2.1',
    author='Ronny Pfannschmidt',
    author_email='opensource@ronnypfannschmidt.de',
    url='http://bitbucket.org/ronny/pytest-cov/',
    license='MIT',
    py_modules=['pytest_cov'],
    entry_points={'pytest11': ['pytest_cov = pytest_cov']},
    install_requires=['pytest>=2.3.5', 'coverage>=3.6'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System ::
