import mmap
import numpy as np
import os
import pytest
import shutil
import uuid
import warnings

from . import test_lib
from .test_lib import tmp_dir


def test_plugin_manager():
    from datmo.core.util.configuration import Configuration
    from datmo.core.util.plugin_manager import PluginManager
    plugin_manager = PluginManager()
    assert isinstance(plugin_manager.configuration, Configuration)


def test_create_new_environment(tmp_dir, monkeypatch, mocker):
    from datmo.core.entity.project import Project
    from datmo.core.util.configuration import Configuration
    from datmo.core.util.plugin_manager import PluginManager
    from datmo.core.util.misc_functions import parse_yaml_from_file
    # Initialize
    configuration = Configuration()
    configuration.set_environment_driver("docker")
