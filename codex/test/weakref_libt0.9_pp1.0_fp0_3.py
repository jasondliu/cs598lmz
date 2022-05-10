import weakref
import logging

from olclient.core.events import EventDispatcher, event_handler
from olclient.core.events import Event
from olclient.core.comms import Client
from olclient.core.context import Context

from olclient.openlibrary import OpenLibrary
from olclient.api import OLAPIRequest

logger = logging.getLogger(__name__)

class ApiManager(EventDispatcher):
    '''
    Maintains a queue of requests and facilitates mapping requests to
    resources, and resources to requests.
    '''
    def __init__(self,context,client):
        super(ApiManager,self).__init__()
        self._context = context
        # Maintain a short request queue, with new requests preempting
        # older ones if a later request matches the resource of an
        # existing request
        self._request_queue = []
        # These dictionaries serve to keep track of the link between
        # resources and requests.
        self._requests_by_resource = {}
        self._resources_by_request = weakref.Weak
