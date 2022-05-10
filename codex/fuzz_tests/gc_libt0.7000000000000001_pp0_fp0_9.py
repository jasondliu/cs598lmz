import gc, weakref
from .utils import *
from .compat import *
from . import namespaces
from . import elements
from . import events

__all__ = ['Document', 'DocumentType', 'Node', 'Element', 'Text',
           'Comment', 'ProcessingInstruction', 'DocumentFragment',
           'Attr', 'NodeList', 'DocumentElement', 'ElementTree',
           'TreeWalker', 'NodeIterator', 'XPath', 'XPathEvaluator',
           'XPathResult']

_log = logging.getLogger("fdom")

class Node(object):
    nodeType = None
    nodeName = None
    nodeValue = None
    parentNode = None
    childNodes = None
    firstChild = None
    lastChild = None
    previousSibling = None
    nextSibling = None
    attributes = None
    ownerDocument = None
    namespaceURI = None
    prefix = None
    localName = None

    def __init__(self, doc, qname=None):
        self.__dict__['_doc'] = doc
        if qname:
