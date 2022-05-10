import weakref
from datetime import datetime, timedelta

import pytest
from freezegun import freeze_time

from cfme import test_requirements
from cfme.common.provider import BaseProvider
from cfme.fixtures.templates import Templates
from cfme.infrastructure.provider.rhevm import RHEVMProvider
from cfme.infrastructure.provider.scvmm import SCVMMProvider
from cfme.infrastructure.provider.virtualcenter import VMwareProvider
from cfme.markers.env_markers.provider import providers
from cfme.utils.log import logger
from cfme.utils.wait import wait_for

pytestmark = [
    pytest.mark.tier(3),
    pytest.mark.long_running,
    pytest.mark.meta(server_roles="+automate"),
    pytest.mark.ignore_stream("upstream"),
    pytest.mark.provider(gen_func=providers,
                         filters=[BaseProvider.type_infra],
                         required_fields=[['templates', '
