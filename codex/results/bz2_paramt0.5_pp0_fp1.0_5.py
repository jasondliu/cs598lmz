from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, data: (
    BZ2Decompressor.decompress(self, data) +
    BZ2Decompressor.flush(self)
)

from lxml import etree

from StringIO import StringIO

from lxml.etree import XMLSyntaxError

from Products.CMFCore.utils import getToolByName

from Products.CMFPlone.utils import safe_unicode

from plone.i18n.normalizer.interfaces import IIDNormalizer

from zope.component import getUtility

from zope.component import getMultiAdapter

from zope.component.hooks import getSite

from zope.globalrequest import getRequest

from z3c.relationfield import RelationValue

from zope.intid.interfaces import IIntIds

from zope.app.intid.interfaces import IIntIds

from zope.component import getUtility

from plone.app.textfield.value import RichTextValue

from plone.namedfile.file import Named
