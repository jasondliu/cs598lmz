import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _util
from . import _util_common
from . import _util_html
from . import _util_html_common
from . import _util_html_elements
from . import _util_html_entities
from . import _util_html_parser
from . import _util_html_writer
from . import _util_js
from . import _util_js_common
from . import _util_js_parser
from . import _util_js_writer
from . import _util_py
from . import _util_py_common
from . import _util_py_parser
from . import _util_py_writer
from . import _util_xml
from . import _util_xml_common
from . import _util_xml_elements
from . import _util_xml_entities
from . import _util_xml_parser
from . import _util_xml_writer

from ._util import *
from ._util_common import *
from ._util_html import *
from ._util_html_common import *

