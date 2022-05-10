import codecs
codecs.register(codecs.lookup('utf-8') if codecs.lookup('utf-8') else codecs.lookup('cp1252'))

from setuptools import setup

with open('README.rst', 'r') as readme_file:
    long_description = readme_file.read()

with open('requirements.txt', 'r') as requirements_file:
    install_requires = requirements_file.read().splitlines()

setup(
    name='python-madkudu',
    version='0.1.0',
    description='A Python client for the Madkudu API',
    long_description=long_description,
    url='https://github.com/madkudu/python-madkudu',
    author='Joshua Nussbaum',
    author_email='josh@madkudu.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language
