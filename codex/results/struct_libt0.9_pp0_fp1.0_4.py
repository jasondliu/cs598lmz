import _struct
import threading

try:
    from . import plugin
except:
    import plugin
from . import general
from . import public_interface

from .query import query_audit_log
from .util import python_24_compatible, hooks_dictionary
from .errors import ManholeError
from . import fake_select
from .encryption import get_context

from . import environment
from .environment import is_py3k
from struct import calcsize, unpack, pack


# not used anymore
def is_authenticated(peer_address=None, username=None, certificate=None):
    """Documentation: Check if the user is authenticated by the certificate

    - peer_address: IP address of the client
    - username: username of the client
    - certificate: client certificate

    Return: True if the user is authenticated
    """
    # no import needed because we have only one module
    # it's this module!
    return True


# not used anymore
def get_manhole_access_for_user(username, role, peer_address=None,
                                certificate=None):
