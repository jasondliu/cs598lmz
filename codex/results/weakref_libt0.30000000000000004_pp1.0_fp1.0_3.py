import weakref

from . import _base
from . import _util
from . import _errors

from . import _compat as _c

__all__ = ['Connection']

class Connection(_base.Connection):
    """Connection to a PostgreSQL database"""

    def __init__(self, *args, **kwargs):
        """Constructor

        :param str host: Host to connect to.
        :param int port: Port to connect to.
        :param str user: User to connect as.
        :param str password: Password to use.
        :param str database: Database to connect to.
        :param bool ssl: Use SSL.
        :param bool ssl_verify: Verify SSL certificate.
        :param str ssl_cert: SSL certificate file.
        :param str ssl_key: SSL key file.
        :param str ssl_root_cert: SSL root certificate file.
        :param str ssl_crl: SSL certificate revocation list file.
        :param str application_name: Application name.
        :param str fallback_application_name: Fallback application name.
