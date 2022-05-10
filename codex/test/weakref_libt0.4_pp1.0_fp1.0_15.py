import weakref

from twisted.internet import defer
from twisted.python import log

from otter.cloud_client import TenantScope
from otter.constants import ServiceType
from otter.util.deferredutils import unwrap_first_error, unwrap_deferred_pool
from otter.util.http import APIError, RequestError
from otter.util.retry import (
    retry,
    retry_times,
    retry_with_timeout,
    retry_with_timeout_sibling,
    retry_times_with_timeout_sibling)
from otter.util.timestamp import from_timestamp

