import codecs
codecs.register_error('strict', codecs.ignore_errors)

from sre import Scanner
from sre import error as sreError
from posixpath import basename, dirname, join, isabs
from os.path import curdir, exists, isfile, normpath
from regex import regex
from urlparse import urlparse, urlunparse, urljoin, urlsplit
from itertools import tee
from urllib import quote
from re import sub as _sub, escape as _escape

from pyglet.media.exceptions import MediaDecodeException
from pyglet.media.sources.base import BaseSource
from pyglet.media.codecs import BaseDecoder, create_audio_format

class Parser(object):
    """
    Scans URLs to find a source of the media data.  Use an instance of this class
    to parse media URIs.

    To create your own parsers, subclass this class and add it to :py:data:`_protocols`.

    .. versionchanged:: 1.2
        The :py:meth:`parse` method now accepts a
