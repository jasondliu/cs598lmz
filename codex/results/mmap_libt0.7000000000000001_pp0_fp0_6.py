import mmap
import os
import re

from avocado.utils import process
from avocado.utils import path as utils_path

from virttest import utils_misc
from virttest import utils_memory
from virttest import utils_selinux
from virttest import error_context
from virttest import data_dir


def get_expected_numa_nodes(numa_node_cpus):
    """
    Get expected numa nodes information.

    :param numa_node_cpus: Cpus info of each numa node.
    :return: A dict like {node_id: [cpus]}
    """
    expected_numa_nodes = {}
    for idx, cpus in enumerate(numa_node_cpus):
        expected_numa_nodes[idx] = list(map(int, cpus))
    return expected_numa_nodes


def verify_numa_node_cpus(test, params, env):
    """
    Verify numa configuration in guest.

    :param test: KVM
