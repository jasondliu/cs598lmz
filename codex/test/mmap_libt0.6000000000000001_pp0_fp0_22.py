import mmap
import os
import pytest
import re
import subprocess
import sys
import time
import yaml

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# These globals are used to store information between test runs
# Don't change them manually
g_config = None


def get_config():
    """
    Get configuration from the Ansible playbook
    :return:
    """
    global g_config
    if g_config is not None:
        return g_config

    # Read config
    current_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(current_dir, '../../molecule/default/playbook.yml')
