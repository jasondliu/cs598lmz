import codecs
# Test codecs.register_error("ignore", codecs.ignore_errors)

from xml.sax import saxutils
from xml.sax.saxutils import XMLGenerator
from xml.sax.xmlreader import AttributesNSImpl
from xml.sax.handler import feature_namespaces

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from itertools import izip_longest
except ImportError:
    from itertools import zip_longest as izip_longest

__all__ = [
    # constants
    "XML_NAMESPACE", "XLINK_NAMESPACE", "XSI_NAMESPACE", "XSD_NAMESPACE",
    "ET_NAMESPACE",

    # exceptions
    "XMLGeneratorError", "XMLGeneratorWarning", "MissingElementName",
    "MissingAttributeName", "NoNamespace", "XMLSchemaError", "XMLSchemaWarning",
    "XMLSchemaParseError", "XMLSchemaIncludeError",
