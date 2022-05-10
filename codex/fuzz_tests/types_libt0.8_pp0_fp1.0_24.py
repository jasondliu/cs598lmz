import types
types.ModuleType.__repr__ = lambda self: '<{} module at 0x{:x}>'.format(self.__name__, id(self))
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

import sphinx.ext
# extensions = ['sphinx.ext.doctest', 'sphinx.ext.coverage', 'sphinx.ext.mathjax', 'nbsphinx']
extensions = ['sphinx.ext.doctest', 'sphinx.ext.coverage', 'sphinx.ext.mathjax', 'sphinx.ext.napoleon', 'nbsphinx']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es
