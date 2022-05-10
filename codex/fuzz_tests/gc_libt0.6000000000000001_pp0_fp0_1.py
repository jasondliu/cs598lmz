import gc, weakref

from webob import Request
from webob import exc
from webob import Response


__all__ = ['WSGIApplication']

class WSGIApplication(object):
    """
    Base WSGI application.
    
    It provides:
    
        * Router
        * Middleware
        * Configuration
        * Template system
        * Session
        * Cache
        * Database connection
        * Localization
        * Static file serving
    
    It is the base class for all WSGI applications.
    
    """
    
    #: Default configuration for the application.
    config = {}
    
    #: A dictionary of routes.
    routes = {}
    
    #: Default middleware.
    middleware = []
    
    #: Default template engine, ``None`` for no template engine.
    template_engine = None
    
    #: Default session engine, ``None`` for no session.
    session_engine = None
    
    #: Default cache engine, ``None`` for no cache.
    cache_engine = None
    
    #: Default database engine
