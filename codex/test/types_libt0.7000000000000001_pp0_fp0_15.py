import types
types.ModuleType('mock')

from mock import Mock
from mock import patch

from oslo_config import fixture as config_fixture
from oslo_db import exception as db_exception
from oslo_utils import uuidutils
from oslo_utils import timeutils

from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan

from magnum.api.controllers.v1 import bay as api_bay
from magnum.api.controllers.v1 import bay_model as api_bay_model
from magnum.api.controllers.v1 import bay_type as api_bay_type
from magnum.api.controllers.v1 import cert as api_cert
from magnum.api.controllers.v1 import cluster as api_cluster
from magnum.api.controllers.v1 import cluster_template as api_cluster_template
from magnum.api.controllers.v1 import cluster_template_host_registry as \
    api_cluster_template_host_registry
