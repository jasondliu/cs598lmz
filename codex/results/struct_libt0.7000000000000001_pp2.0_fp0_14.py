import _struct
import sys
import time

_PY2 = sys.version_info[0] == 2
if _PY2:
    from itertools import izip as zip

##
# The following URL is for the official wxWidgets documentation, which is
# often more up to date than what is included in the wxWidgets releases themselves.
_WX_WIDGETS_DOC_URL = 'http://docs.wxwidgets.org/stable/'

##
# The following URL is used to fetch the latest version of the wxWidgets API
# documentation.
_WX_WIDGETS_API_DOC_URL = 'http://docs.wxwidgets.org/api/'

##
# The following URL is used to download the specific class information for a
# particular class in the wxWidgets API documentation.
_WX_WIDGETS_CLS_DOC_URL = 'http://docs.wxwidgets.org/api/class'

##
# This is used to generate the docs for the specific version of the wxWid
