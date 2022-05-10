import weakref

from zope.component.factory import Factory
from zope.interface import implements, implementer
from zope.interface.interfaces import IInterface
from zope.interface.adapter import AdapterRegistry
from zope.interface.adapter import _createLookup
from zope.interface.declarations import getObjectSpecification
from zope.interface.declarations import ObjectSpecificationDescriptor

from pyramid.interfaces import IRequest
from pyramid.interfaces import IResponse
from pyramid.interfaces import IRootFactory
from pyramid.interfaces import IView
from pyramid.interfaces import IViewClassifier
from pyramid.interfaces import IViewMapperFactory
from pyramid.interfaces import IViewPermission
from pyramid.interfaces import IRequestFactory
from pyramid.interfaces import IResponseFactory
from pyramid.interfaces import IExceptionResponse
from pyramid.interfaces import IExceptionViewClassifier
from pyramid.interfaces import IExceptionViewMapper
from pyramid.interfaces import IRendererFactory
from pyramid.interfaces import IChameleonLookup
from pyramid.interfaces import IStaticURLInfo
