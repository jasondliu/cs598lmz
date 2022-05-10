import weakref

from zope.interface import implements
from zope.component import getMultiAdapter, queryMultiAdapter

from z3c.form import field
from z3c.form.interfaces import IFormLayer

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from plone.indexer import indexer

from plone.app.content.interfaces import INameFromTitle
from plone.app.layout.viewlets import content

from plone.app.contenttypes.interfaces import IFile
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.navigation.root import getNavigationRoot
from plone.app.layout.navigation.root import getNavigationRootObject

from plone.app.contenttypes.behaviors.leadimage import ILeadImage
from plone.app.contenttypes.behaviors.leadimage import ILeadImageMarker
from plone.app.contenttypes.
