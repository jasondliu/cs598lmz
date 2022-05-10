import gc, weakref
from weakref import WeakKeyDictionary

from zope.interface import implements
from zope.component import getAdapter, getAdapters

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base, aq_inner, aq_parent
from App.class_init import InitializeClass
from Globals import InitializeClass as InitializeClassGlobal

from Products.Archetypes.config import REFERENCE_ANNOTATION, REFERENCE_CATALOG, UID_ATTR
from Products.Archetypes.interfaces.referenceable import IReferenceable
from Products.Archetypes.referenceengine import _resolve_path
from Products.Archetypes.utils import shasattr
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException


_marker = []

def manage_addReferenceable(obj, REQUEST=None):
    """This is the only way to add Referenceable to an object now.
    """
    obj.addReference(rel="Referenceable", target=obj)

def manage_addReference
