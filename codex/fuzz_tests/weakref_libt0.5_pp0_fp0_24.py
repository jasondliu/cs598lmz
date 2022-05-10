import weakref
import collections

from zope.interface import implements, Interface
from zope.component import getMultiAdapter

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from Products.Collage import CollageMessageFactory as _
from Products.Collage.interfaces import ICollageEditLayer
from Products.Collage.interfaces import ICollageDisplayLayer
from Products.Collage.browser.interfaces import ICollageRowView
from Products.Collage.browser.interfaces import ICollageView
from Products.Collage.browser.interfaces import ICollageRowEdit
from Products.Collage.browser.interfaces import ICollageEdit
from Products.Collage.browser.interfaces import ICollageDebug
from Products.Collage.browser.interfaces import ICollageJavascript
from Products.Collage.browser.interfaces import ICollageCSS
from Products.Collage.
