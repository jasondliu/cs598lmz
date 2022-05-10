import socket
import dill

from pyrevitmep.loaders import Loader
from pyrevitmep.utils import log, logger
from pyrevitmep.param_utils import Param
from pyrevitmep.branches import Branch

from pyrevitmep.ui.exceptions import BimServerException, BimServerConnectionException
from pyrevitmep.config import project_config
from pyrevitmep.config import configuration
from pyrevitmep.ui.branch_ui import push_to_repository
from pyrevitmep.ui.exceptions import MepException
from pyrevitmep.ui.config_ui import config_optional_parameters_ui, user_config_manager_ui

import pyrevitmep as mep


def connect_to_bimserver():
    """Subscribes to the bimserver api
    :return: subscription
    """
