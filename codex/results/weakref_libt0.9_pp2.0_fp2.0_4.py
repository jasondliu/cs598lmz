import weakref
import os

import rafcon.utils.vividict as xdict
from rafcon.core.execution.execution_engine import ExecutionEngine

from rafcon.core.states.state import State
from rafcon.core.singleton import state_machine_manager

from rafcon.utils import log
logger = log.get_logger(__name__)

# the key in the state "data" dict (value = weakref.prt(instance))
STATE_INSTANCE_KEY = "state_instance"

########################################################################################################################

# global lifetime of observer
_execution_observer_instance = None

def _get_observer_instance():
    global _execution_observer_instance
    if not _execution_observer_instance:
        _execution_observer_instance = Observer()
    return _execution_observer_instance

########################################################################################################################

def receive_notification(signal_name, data, operation_id=None, **kwargs):

    observer = _get_observer_instance()
