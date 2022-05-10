import types
types.FunctionType = types.BuiltinFunctionType
types.MethodType = types.FunctionType

import collections
import contextlib
import logging
import os
import sys

import mock
import pytest
import pytz

from ceph.deployment import inventory
from ceph.deployment.drive_group import DriveGroupSpec, DeviceSelection
from ceph.deployment.service_spec import ServiceSpec, PlacementSpec, \
    RGWSpec, NFSServiceSpec, IscsiServiceSpec
from orchestrator import OrchestratorError, DaemonDescription, \
    OrchestratorValidationError, HostSpec, ServiceDescription
from orchestrator import OrchestratorImageFormat
from orchestrator import OrchestratorInventoryFilter
from tests import mock
from tests.fixtures.cephfs import CephFSTestCluster
from tests.fixtures.iscsi import IscsiTestCluster
from tests.fixtures.nfs import NFSTestCluster
from tests.fixtures.rgw import RGWTestCluster
from tests.fixtures.rgw import RGWSyncTestCluster
