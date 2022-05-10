import weakref
import lxml.etree
from html import unescape

from .directory import CACHE_DIR, PATHS, NAMESPACES, sys_cachefile


class ArgumentsError(Exception):
    pass


def escape(text, attr=False, special=False, link=False):
    """Process text, escape special chars, etc."""

    text = ''.join(text.splitlines())
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = text.replace('\\', '\\\\')

    if attr:
        text = text.replace('\'', '&apos;')

    if special:
        text = text.replace('{', '\{')
        text = text.replace('}', '\}')
        text = text.replace('_', '\_')
        text = text.replace('$', '\$')
        text
