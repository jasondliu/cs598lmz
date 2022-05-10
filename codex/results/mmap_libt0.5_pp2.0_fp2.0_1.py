import mmap
import os
import re
import sys
import time
import traceback
import warnings

from collections import namedtuple

from .compat import (
    compat_str,
    compat_urllib_error,
    compat_urllib_parse,
    compat_urllib_request,
    compat_urllib_response,
    compat_urlparse,
    compat_cookiejar,
    compat_http_client,
    compat_struct_pack,
    compat_struct_unpack,
    compat_etree_fromstring,
    compat_etree_ElementTree,
    compat_etree_tostring,
    compat_etree_parse,
    compat_etree_register_namespace,
    compat_etree_QName,
    compat_etree_Element,
    compat_etree_SubElement,
    compat_etree_iterparse,
    compat_urllib_parse_urlencode,
    compat_urllib_parse_urlparse,
    compat_urllib_parse_unquote,
    compat_
