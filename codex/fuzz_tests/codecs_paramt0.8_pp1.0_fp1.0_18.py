import codecs
codecs.register_error("xmlcharrefreplace", xmlcharrefreplace_error)

import sys
import os
import platform
import traceback
import re

from . import log
from . import file
from . import pprint
from . import config
from . import html
from . import data
from . import error
from . import lang
from . import util
from . import css
from . import js
from . import version
from . import sip
from . import test

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    _test()
