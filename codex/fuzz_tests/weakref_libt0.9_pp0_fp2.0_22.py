import weakref

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from hyperadmin.clients.common import ResourceListing
from hyperadmin.sites import HyperAdminSite

from ..base import BaseEndpoint, BaseLink
from ..response import Response
from ..routers import SimpleRouter
from ..serializers import get_serializer_class
from ..signals import request_finished


class ResourceEndpoint(BaseEndpoint):
    """
    A ResourceLinks endpoint that allows the registration of ResourceLinks
    """
    slug = 'resource'
    default_link_protocol = 'resources'
    request_handler_class = ResourceEndpoint

    def __init__(self, *args, **kwargs):
      self.signals = {}
      super(ResourceEndpoint, self).__init__(*args, **kwargs)

    def get_link_protocol(self, link):
        protocol = link.protocol or self.default_link_protocol
        protocol_cls = self
