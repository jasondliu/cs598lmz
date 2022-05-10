import types
types.ModuleType.__setattr__ = _mock_setattr

import unittest
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import patch

from botocore.exceptions import ClientError
from mock import ANY

from stacker.lookups.handlers.secretsmanager import SecretsManager
from stacker.blueprints.testutil import (
    BlueprintTestCase,
    generate_definition,
)
from stacker.exceptions import (
    InvalidLookupException,
    StackDoesNotExist,
    StackOutputDoesNotExist,
    StackOutputLookupFailed,
)
from stacker.lookups.handlers.output import Output
from stacker.lookups.handlers.output import OutputLookup
from stacker.lookups.registry import LookupRegistry
from stacker.session_cache import get_session
from stacker.tests import StackOutputFixture

from botocore.exceptions import ClientError


class TestOutputLookup(BlueprintTestCase):
    def setUp(self):
