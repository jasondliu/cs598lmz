import weakref

from django.core.exceptions import FieldDoesNotExist
from django.utils.encoding import smart_unicode
from django.utils.functional import Promise
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from neutronclient.common import exceptions as neutron_exceptions

from horizon.utils.memoized import memoized  # noqa
from openstack_dashboard.api import base
from openstack_dashboard.api import cinder
from openstack_dashboard.api import nova
from openstack_dashboard.api import neutron
from openstack_dashboard.api.rest import urls
from openstack_dashboard.api.rest import utils as rest_utils

# Some of the following libraries may not be available if swift is not enabled
try:
    from swiftclient import client as swift
except ImportError:
    swift = None

try:
    from manilaclient import client as manila
except ImportError:
    manila = None

try:
    from troveclient import
