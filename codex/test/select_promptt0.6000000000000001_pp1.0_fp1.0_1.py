import select
# Test select.select
import socket
import sys
import time

try:
    import uuid
except ImportError:
    uuid = None

from certbot import errors
from certbot import interfaces
from certbot import util

from certbot.plugins import common


logger = logging.getLogger(__name__)


class Authenticator(common.Plugin):
    """Apache Authenticator."""

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.config = util.get_apache_configurator(
            self.config, self.config.http01_port, self.config.tls_sni_01_port)
        self.version = self.config.version
        self.parser = self.config.parser
        self.vhost = None
        self.challenge_conf = dict()

    def prepare(self):  # pylint: disable=missing-docstring,no-self-use
        pass  # pragma: no cover
