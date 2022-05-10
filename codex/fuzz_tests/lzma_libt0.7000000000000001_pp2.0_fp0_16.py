import lzma
lzma.__file__

import uuid
from unittest.mock import MagicMock
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.utils.vars import combine_vars
from ansible.utils.vars import load_extra_vars
from ansible.utils.vars import load_options_vars
from ansible.plugins.callback import CallbackBase
from ansible import constants as C
from ansible import context
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_result import TaskResult
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.json import CallbackModule
from ansible.plugins.callback.yaml import CallbackModule as YamlCallbackModule
from ansible.plugins.callback.
