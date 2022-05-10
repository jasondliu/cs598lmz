import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from setuptools import setup
import os

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

from geonode import version as geonode_version

setup(
    name='geonode-user-messages',
    version=geonode_version,
    packages=['geonode_user_messages'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A Django app for user messages.',
    long_description=README,
    url='https://github.com/GeoNode/geonode-user-messages',
    author='GeoNode Developers',
    author_email='dev@
