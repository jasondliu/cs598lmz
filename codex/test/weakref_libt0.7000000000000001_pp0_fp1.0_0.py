import weakref

from lxml import etree

from .errors import ValidationError, ParseError

from . import fields as f
from . import utils
from . import validators as v

from .reader import Reader
from .writer import Writer
from .opener import Opener


try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


_log = logging.getLogger(__name__)


__all__ = [
    'Document',
    'Namespace',
    'DocumentPart',
    'ParagraphPart',
    'RunPart',
    'HyperlinkPart',
    'InlineShapes',
    'TablePart',
    'TableCellPart',
    'TableRowPart',
    'ListPart',
    'ListItemPart',
    'HeaderPart',
    'FooterPart',
    'PageBreak',
    'AnnotationPart',
    'FieldPart',
    'BookmarkPart',
    'ImagePart',
    'ShapePart',
    'chart'
]

