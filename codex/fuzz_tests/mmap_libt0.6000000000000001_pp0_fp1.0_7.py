import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile

from collections import namedtuple
from contextlib import contextmanager
from functools import partial
from io import StringIO
from itertools import chain
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

from mypy_boto3_builder.common import (
    Boto3BuilderConfig,
    BuildStatus,
    Config,
    ConfigValue,
    Data,
    DataKey,
    DEFAULT_CONFIG_PATH,
    DEFAULT_DATA_PATH,
    DEFAULT_MODULE_NAME,
    Module,
    ModuleDependencies,
    ModuleName,
    ModulePath,
    ModuleVersion,
    PYTHON_VERSION,
    Service,
    ServiceName,
    ServiceVersion,
    Version,
)
from mypy_boto3_builder.import_dst.module
