import weakref
import logging
from .. import IProductInstance
from .interfaces import IContentView
from .interfaces import IProductCollection
from .interfaces import IProductCollectionView
from .interfaces import IProductCollectionViewManager
from .interfaces import IProductInstanceView
from .interfaces import IProductInstanceViewManager
from .interfaces import IProductInstanceViewDefinition
from grokcore.layout.interfaces import IPage
from zope.component import adapter
from zope.component import getUtility
from zope.component import queryUtility
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import providedBy
from zope.security.interfaces import IPermission
from zope.security.proxy import removeSecurityProxy

logger = logging.getLogger('grokui.admin')

@adapter(IProductCollection, IPage)
def getProductCollectionView(collection, request):
    """A view name for a collection will be resolved to an actual
    view component by looking up a view component
