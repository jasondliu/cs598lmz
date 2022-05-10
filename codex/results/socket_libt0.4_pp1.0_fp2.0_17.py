import socket

from . import common
from . import constants
from . import exceptions
from . import utils
from . import __version__


class Client(object):
    """
    A client for the Amazon Simple Queue Service.
    """

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
                 is_secure=True, port=None, proxy=None, proxy_port=None,
                 proxy_user=None, proxy_pass=None, debug=0,
                 https_connection_factory=None, region=None,
                 path='/', security_token=None,
                 suppress_consec_slashes=True,
                 anon=False,
                 validate_certs=True, profile_name=None):
        """
        Create a new client to the Amazon Simple Queue Service.

        :type aws_access_key_id: string
        :param aws_access_key_id: Your AWS Access Key ID

        :type aws_secret_access_key: string
        :param aws
