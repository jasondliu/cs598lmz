import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import dirname, join

from setuptools \
    import setup, find_packages

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The directory containing this setup.py file:
root_dir = dirname( __file__ )

# The text of the README file:
with codecs.open( join( root_dir, 'README.rst' ), encoding = 'utf-8' ) as f:
    long_description = f.read()

#-------------------------------------------------------------------------------
#  'setup' function:
#-------------------------------------------------------------------------------

setup(
    name             = 'pyface',
    version          = '6.0.0',
    author           = 'Enthought, Inc',
    author_email     = 'info@enthought.com',
    maintainer       = 'ETS Developers',
    maintainer_email = 'enthought-dev@enthought.com',
    url              = 'https://github.com/enth
