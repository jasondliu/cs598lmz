import weakref

from pulsar import ispy3k, iscoroutinefunction, coroutine
from pulsar.utils.httpurl import (
    is_absolute_uri, uri_to_iri, iri_to_uri,
    parse_qs, urlencode, uri_parser, uri_validator
)


__all__ = ['HttpWsgiRequest',
           'HttpWsgiResponse',
           'HttpWsgiProtocol',
           'WsgiResponse',
           'WsgiParser',
           'get_wsgi_environ',
           'PulsarWSGIServer',
           'WsgiResponse']


if ispy3k:
    def str_bytes(value, encoding=None):
        if isinstance(value, bytes):
            return value
        elif isinstance(value, str):
            return value.encode(encoding or 'utf-8')
        else:
            return str(value).encode(encoding or 'utf-8')
else:
    def str_bytes(value, encoding=None):
        if isinstance(value, unicode
