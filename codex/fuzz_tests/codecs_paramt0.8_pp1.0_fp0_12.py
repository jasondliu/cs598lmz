import codecs
codecs.register_error('strict', codecs.ignore_errors)

from plone.app.linkintegrity.exceptions import LinkIntegrityNotificationException
from plone.memoize.view import memoize
from plone.memoize.view import memoize_contextless
from plone.namedfile.file import NamedBlobImage
from plone.registry.interfaces import IRegistry
from plone.z3cform import z2
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.browser.navigation import get_view_url
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getFSVersionTuple
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.global
