import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
import io
# Test io.StringIO
import pickle
# Test pickle.load
import sys
# Test sys.getdefaultencoding

from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.core.management.base import OutputWrapper
from django.core.management.color import color_style
from django.core.management.commands.loaddata import (
    Command as LoadDataCommand,
    SingleZipReader,
)
from django.core.management.sql import (
    emit_post_migrate_signal,
    emit_pre_migrate_signal,
)
from django.db import connections, DEFAULT_DB_ALIAS
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.recorder import MigrationRecorder
from django.db.migrations.state import ProjectState
from django.test import (
    SimpleTestCase, skipUnlessDBFeature,
