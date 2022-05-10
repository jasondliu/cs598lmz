import weakref

from twisted.python import log

from pyipmi.errors import DecodingError, EncodingError, RetryableError
from pyipmi.msgs import create_request_by_name, decode_response_by_name
from pyipmi.utils import check_completion_code


class Command(object):
    """
    Represents a command to be sent to the BMC.

    Attributes:
        name (str): Name of the command.
        request (pyipmi.msgs.message.Request): Request message object.
        response (pyipmi.msgs.message.Response): Response message object.
    """

    def __init__(self, name, request, response):
        self.name = name
        self.request = request
        self.response = response


class Request(object):
    """
    Represents a request to be sent to the BMC.

    Attributes:
        command (pyipmi.transport.Command): Command object.
        request (pyipmi.msgs.message.Request): Request message object.
        response (pyipmi.msgs.
