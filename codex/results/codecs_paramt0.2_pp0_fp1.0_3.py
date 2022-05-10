import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, abspath

from setuptools \
    import setup, find_packages

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The directory containing this setup.py file:
root_dir = abspath( dirname( __file__ ) )

# The text of the README.txt file:
with codecs.open( join( root_dir, 'README.txt' ), encoding = 'utf-8' ) as file:
    long_description = file.read()

#-------------------------------------------------------------------------------
#  'setup' function:
#-------------------------------------------------------------------------------

setup(
    name             = 'envisage.plugins.remote_editor',
    version          = '4.5.0',
    author           = 'Enthought, Inc',
    author_email     = 'info@enthought.com',
    url              = 'https://github.com/enthought/envisage.plugins.remote_editor',

