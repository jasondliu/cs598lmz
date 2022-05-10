import codecs
codecs.register_error('strict', codecs.ignore_errors)

# from . import __version__
__version__ = '0.0.1'

# from . import __author__
__author__ = 'Javier Domingo Cansino <javierdo1@gmail.com>'

# from . import __author_email__
__author_email__ = 'javierdo1@gmail.com'

# from . import __license__
__license__ = 'GPLv3'

# from . import __url__
__url__ = 'http://github.com/javierdo1/pytesseract'

# from . import __copyright__
__copyright__ = 'Copyright (c) 2014, Javier Domingo Cansino <javierdo1@gmail.com>'

# from . import __doc__
__doc__ = '''
Python-tesseract is a wrapper for Google's Tesseract-OCR Engine.
It is also useful as a stand-alone invocation script to tesseract,
as it can read all image types supported by the Pillow and
