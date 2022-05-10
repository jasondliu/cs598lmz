import mmap
import os
import re
import shutil
import sys
import tempfile
import textwrap
import time
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlparse

from . import __version__
from .exceptions import (
    AnsibleError,
    AnsibleFileNotFound,
    AnsibleOptionsError,
    AnsibleParserError,
    AnsibleUndefinedVariable,
)
from .parsing.dataloader import DataLoader
from .parsing.vault import VaultLib
from .plugins.loader import PluginLoader
from .plugins.vars.manager import VariableManager
from .utils.collection_loader import AnsibleCollectionLoader
from .utils.collections_loader_cache import AnsibleCollectionsLoaderCache
from .utils.config import (
    ANSIBLE_CONFIG_ENV_VAR,
    DEFAULTS,
    ConfigManager,
    get_config,
    load_config_file,
)
from .utils.display import Display
from .utils.module_docs import get_docstring
from
