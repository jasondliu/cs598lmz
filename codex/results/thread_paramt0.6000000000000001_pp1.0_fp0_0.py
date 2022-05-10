import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import unittest
import requests
import requests_mock
from requests.exceptions import ConnectionError
import json
from mock import MagicMock
from mock import patch

from f5_openstack_agent.lbaasv2.drivers.bigip.icontrol_driver import (
    iControlDriver
)

from f5_openstack_agent.lbaasv2.drivers.bigip.resource_helper import \
    ResourceType

import logging
from f5_openstack_agent.lbaasv2.drivers.bigip.icontrol_driver import log

from f5_openstack_agent.lbaasv2.drivers.bigip.service_adapter import \
    ServiceModelAdapter
from f5_openstack_agent.lbaasv2.drivers.bigip.service_adapter import \
    ServiceAdcResourceNotFound
from f5_openstack_agent.lbaasv2.drivers.bigip.service_adapter import \
    ServiceAdcResourceExists
