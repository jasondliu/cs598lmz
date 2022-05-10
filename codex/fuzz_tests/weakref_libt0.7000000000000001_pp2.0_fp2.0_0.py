import weakref

from twisted.internet import defer
from twisted.internet.interfaces import IConsumer, IPushProducer
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import FileSender
from twisted.python import log
from zope.interface import implementer

from txweb.lib.str_request import StrRequest
from txweb.lib.str_response import StrResponse
from txweb.lib.cache import ResponseCache
from txweb.lib.utils import yield_deferred
from txweb.lib._paginate import Pagination, PageNotAnInteger
from txweb.lib.constants import HTTP_VERSION
from txweb.lib.exceptions import RequestNotHandled
from txweb.lib.exceptions import ResponseNotHandled
from txweb.lib.exceptions import RequestHandled
from txweb.lib.exceptions import QuitRequestHandling
from txweb.lib.exceptions import HaltServer
from txweb.lib.exceptions import HttpException
from txweb.lib.exceptions import BadRequest
from txweb.lib.exceptions import NotFound
from txweb.
