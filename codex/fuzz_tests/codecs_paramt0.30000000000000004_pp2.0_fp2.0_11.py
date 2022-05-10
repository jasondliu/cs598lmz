import codecs
codecs.register_error('strict', codecs.ignore_errors)

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='py-pagseguro',
    version='0.1.0',
    description='Python PagSeguro API',
    long_description=readme,
    author='Rafael Henrique da Silva Correia',
    author_email='rafael@correia.io',
    url='https://github.com/rafaelhenrique/py-pagseguro',
    license=license,
    packages=['pagseguro'],
    install_requires=[
        'requests',
        'xmltodict',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
