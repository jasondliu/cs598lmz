import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
#  Copyright (C) 2013  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Stdlib imports
import io
import os
import sys
import re
import warnings
import webbrowser

# Third-party imports
from jinja2 import Environment, FileSystemLoader
from traitlets import Bool, Unicode, Dict, List
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer, TextLexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

# Our own imports
from .base import ConfigurableTransformer
from .transformers import IPythonTransformer
from .filters import markdown_filter, strip_dollars_filter, add_anchor_links, posix_path
from . import
