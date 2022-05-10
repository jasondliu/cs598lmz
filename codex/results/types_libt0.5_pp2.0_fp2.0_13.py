import types
types.ModuleType.__dict__ = dict

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from mock import Mock, patch

from pecan import expose, request
from pecan.hooks import PecanHook
from pecan.tests import PecanTestCase

from pyfarm.models.core.types import db
from pyfarm.models.core.types import setup_db
from pyfarm.models.user import User
from pyfarm.models.job import Job

from pyfarm.master.application import setup_app
from pyfarm.master.api.v1.users import UsersController
from pyfarm.master.api.v1.users import UsersRootController
from pyfarm.master.api.v1.jobs import JobsController
from pyfarm.master.api.v1.jobs import JobsRootController

from pyfarm.master.api.
