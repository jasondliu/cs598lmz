import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from contextlib import contextmanager
from distutils.spawn import find_executable
from itertools import islice
from typing import Iterable

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.db.migrations.loader import MigrationLoader
from django.db.migrations.recorder import MigrationRecorder
from django.db.utils import OperationalError
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.functional import cached_property

from ... import __version__


def _build_version(version):
    # type: (str) -> str
    """
    Constructs a full version string using the given version and the current
    Django version.
    """
    return "%s (Django %s)" % (version, get_django_version())


def get
