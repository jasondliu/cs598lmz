import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from distutils.version import StrictVersion

from charmhelpers.core.hookenv import (
    config,
    log,
    relation_ids,
    related_units,
    relation_get,
    relation_set,
    status_set,
    unit_get,
    is_leader,
    leader_get,
    leader_set,
    leader_set_flag,
    leader_get_flag,
    is_relation_made,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
)

from charmhelpers.core.host import (
    adduser,
    add_group,
    add_user_to_group,
    mkdir,
    service_restart,
    service_stop,
    service_start,
    service_running,
    pwgen,
    lsb_release,
    CompareHostReleases,
    is_container,
)

from charmhelpers.fetch import (

