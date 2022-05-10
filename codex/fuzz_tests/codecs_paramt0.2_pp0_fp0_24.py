import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join

from distutils.core \
    import setup

from distutils.command.install_data \
    import install_data

from distutils.command.install \
    import INSTALL_SCHEMES

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The base package metadata to be used by both distutils and setuptools:
METADATA = dict(
    name         = 'envisage',
    version      = '3.0.0',
    author       = 'Enthought, Inc',
    author_email = 'info@enthought.com',
    maintainer   = 'ETS Developers',
    maintainer_email = 'enthought-dev@enthought.com',
    url          = 'https://github.com/enthought/envisage',
    download_url = ('http://www.enthought.com/repo/ets/envisage-%s.tar.gz' %

