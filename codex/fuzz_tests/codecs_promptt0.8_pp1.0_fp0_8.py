import codecs
# Test codecs.register_error('decode_error', 'replace')
from optparse import OptionParser
from sys import stderr
import xml.dom.minidom

from . import compat
from .compat import unichr
from . import const
from .const import (
    XMLNS_ATTR,
    XHTML_TAGS,
    XML_CONVERT_TAGS, XHTML_NAMESPACE,
    XHTML_CLOSE_TAGS_NAMESPACE,
    XML_EMPTY_TAGS,
    XHTML_NAMESPACES,
    XHTML_NAMESPACE_URL_MAP,
    XHTML_DEFAULT_NAMESPACE,
    XHTML_REPLACEMENT_NAMESPACE,
    XHTML_DEFAULT_NAMESPACE_URL,
    XHTML_REPLACEMENT_NAMESPACE_URL,
    NAMESPACE_ATTR,
    XHTML_ENTITIES,
    MINIDOM_ENTITIES,
    REPLACEMENT_ENTITIES,
    ENTITIES,
    NUM2ENTITY,
    XHTML_N
