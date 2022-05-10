import codecs
codecs.register_error('compat', lambda e, x: (x.decode('latin1'), x.encode('latin1')))

from pygments import lexers, formatters, filters
from pygments.text import Text

from twisted.web import server
from twisted.web.resource import Resource
from twisted.web.util import redirectTo
from twisted.web.template import Element, XMLFile, renderer, \
                                 XMLString, flattenString, \
                                 tags, TagLoader, renderElement
from twisted.web.template import renderSynchronously, tags as t

from nevow import inevow, url, loaders, stan
from nevow.util import unicode
from nevow.context import WovenContext
from nevow.static import File, FileServeFactory
from nevow.livepage import LivePage
from nevow.appserver import NevowSite
from nevow.url import root, URL
from nevow.loaders import xmlfile
from nevow.loaders import stan as stanloader
from nevow.rend import Page
from
