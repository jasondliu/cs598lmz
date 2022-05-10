import weakref
from zope.interface import implements, noLongerProvides

from Globals import DTMLFile
from Globals import InitializeClass
from Globals import MessageDialog
from AccessControl import ClassSecurityInfo, getSecurityManager

from Acquisition import aq_base, aq_parent
from ComputedAttribute import ComputedAttribute
from DocumentTemplate.DT_Util import TemplateDict, safe_callable
from DocumentTemplate.DT_Util import parse_params
from DocumentTemplate.DT_Util import InstanceDict
from DocumentTemplate.DT_HTML import HTML
from DocumentTemplate.DT_HTML import HTMLFile
from DocumentTemplate.DT_String import String
from DocumentTemplate.security import RestrictedDTML
from Expression import Expression
from ExtensionClass import Base
from MethodObject import Method
from OFS.Cache import Cacheable
from OFS.interfaces import ISimpleItem
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem
from OFS.Cache import zcache
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
