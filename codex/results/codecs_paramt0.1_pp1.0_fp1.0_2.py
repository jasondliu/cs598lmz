import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join

from setuptools \
    import setup, find_packages

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The name of the package:
NAME = 'envisage'

# The version of the package:
VERSION = '3.0.0'

# The release status of the package:
ISRELEASED = False

# The SVN revision of the package:
SVN_REVISION = '$Revision: 7094 $'

# The list of required packages:
REQUIRES = [
    'apptools',
    'traits',
    'traitsui',
    'pyface',
    'pygments',
    'pygments-style-solarized',
    'pygments-style-tango',
    'pygments-style-vim',
    'pygments-style-autumn',
    'pygments-style-borland',
    'py
