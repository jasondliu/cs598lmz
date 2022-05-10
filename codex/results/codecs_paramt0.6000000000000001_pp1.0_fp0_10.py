import codecs
codecs.register_error('strict', codecs.ignore_errors)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyGithub',
    version='1.17',
    author='Jacquelin Charbonnel',
    author_email='jacquelin.charbonnel@gmail.com',
    packages=['github', 'github.tests'],
    package_data={'github': ['tests/data/*.json']},
    scripts=[],
    url='https://github.com/jacquev6/PyGithub',
    license='LICENSE.txt',
    description='Use the full Github API v3.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 0.8.8"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Oper
