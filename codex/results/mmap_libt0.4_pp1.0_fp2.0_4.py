import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

from contextlib import contextmanager
from distutils.version import LooseVersion
from functools import partial
from itertools import chain

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

from olympia import amo
from olympia.amo.utils import rm_local_tmp_dir
from olympia.constants.applications import APPS
from olympia.lib import crypto
from olympia.lib.crypto.packaged import get_key, sign_file, sign_string
from olympia.lib.es.utils import get_indices, reindex_cmd
from olympia.lib.git import AddError, CommitError, GitError, PullError, PushError
from olympia.lib.git.utils import (
    pull_from_git, push_to
