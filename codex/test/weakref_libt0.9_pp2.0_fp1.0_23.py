import weakref
import ansible.constants as C
from ansible.errors import AnsibleParserError
from ansible.parsing import DataLoader
from ansible.playbook.block import Block
from ansible.playbook.handler import Handler
from ansible.playbook.helpers import load_list_of_blocks
from ansible.playbook.role import Role
from ansible.playbook.role.include import RoleInclude
from ansible.playbook.task import Task
from ansible.plugins.loader import get_all_plugin_loaders, filter_loader
from ansible.template import Templar
from ansible.utils.collection_loader import AnsibleCollectionRef
from ansible.utils.display import Display
from ansible.utils.version import (
    t_version_to_info,
    t_semver_to_info,
    version_compare_many,
)
from ansible.utils.vars import combine_vars
from ansible.vars.manager import VariableManager

from ansible_collections.ansible.community.plugins.module_utils._text import to_bytes
