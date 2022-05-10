import types
types.__all__ += ('__version__', '__version_info__', '__author__', '__author_email__', '__description__', '__url__', '__download_url__', '__license__', '__long_description__', '__classifiers__', '__keywords__')


# Variable that stores the version of the types package.
__version__ = '0.1.0'

# Variable that stores the version tuple of the types package.
__version_info__ = tuple(int(num) if num.isdigit() else num for num in __version__.replace('-', '.').split('.'))

# Variable that stores the author of the types package.
__author__ = 'Marcel Hellkamp'

# Variable that stores the email address of the author of the types package.
__author_email__ = 'marc@gsites.de'

# Variable that stores the description of the types package.
__description__ = 'Extension of the types module of the Python standard library.'

# Variable that stores the URL of the types package.
