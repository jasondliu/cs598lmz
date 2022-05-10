import types
types.ListType = list

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from Products.TinyMCE.browser.browser import TinyMCEBrowserView
from Products.TinyMCE.browser.interfaces.browser import ITinyMCESchema
from Products.TinyMCE.browser.interfaces.browser import ITinyMCEBrowserView
from Products.TinyMCE.interfaces.utility import ITinyMCE
from Products.TinyMCE.setuphandlers import DEFAULT_JS_CONTENT
from Products.TinyMCE.setuphandlers import DEFAULT_JS_URL
from Products.TinyMCE.setuphandlers import DEFAULT_LINK_LIST
from Products.TinyMCE.setuphandlers import DEFAULT_IMAGE_LIST
from Products.TinyMCE.setuphandlers import DEFAULT_IMAGE_LIST_URL
from Products.TinyMCE.setuphandlers import DEFAULT_LINK_LIST_URL
from
