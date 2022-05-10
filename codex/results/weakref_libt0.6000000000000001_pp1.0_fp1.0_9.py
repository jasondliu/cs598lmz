import weakref
import abc

from . import config, exceptions
from .utils import (
    is_string,
    is_callable,
)

from .routing import Route, RouteCollection
from .wrappers import Response
from .application import Application
from .request import Request


_sentinel = object()


class BaseHandler(object):
    """
    Base class for all handler types.
    """
    __metaclass__ = abc.ABCMeta

    #: A :class:`werkzeug.routing.Route` instance representing the route
    #: this handler is attached to.
    route = None

    #: The :class:`~apex.application.Application` instance this handler is
    #: associated with.
    application = None

    def __init__(self, route, application, **kwargs):
        self.route = route
        self.application = application

    @abc.abstractmethod
    def __call__(self, request, values):
        """
        Execute this handler for the given request and route values.
        """
        raise NotIm
