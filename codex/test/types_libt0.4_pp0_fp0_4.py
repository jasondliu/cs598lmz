import types
types.ModuleType.__repr__ = lambda self: self.__name__

# -- Project information -----------------------------------------------------

project = 'dask_sql'
copyright = '2020, Tom Augspurger'
author = 'Tom Augspurger'

# The full version, including alpha/beta/rc tags
release = '0.1.0-dev'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
