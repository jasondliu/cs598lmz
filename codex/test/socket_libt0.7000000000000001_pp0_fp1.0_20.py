import socket

from .base import Transport
from .base import TransportError

from .compat import string_types
from .compat import ssl
from .compat import ssl_create_default_context
from .compat import ssl_match_hostname
from .compat import ssl_match_hostname_backport
from .compat import ssl_SSLError
from .compat import ssl_CertificateError
from .compat import ssl_match_hostname_ipaddress
from .compat import ssl_CertificateError_hostname
from .compat import ssl_CertificateError_ipaddress
from .compat import ssl_CertificateError_hostname_ipaddress

from .exceptions import SSLError
from .exceptions import ConnectionClosed


if ssl_match_hostname is None:
    ssl_match_hostname = ssl_match_hostname_backport


