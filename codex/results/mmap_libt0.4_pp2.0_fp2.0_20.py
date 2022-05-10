import mmap
import os
import re
import sys
import tempfile
import time
import zipfile
from io import BytesIO
from os.path import basename, dirname, exists, join, normpath, splitext
from shutil import copyfileobj
from subprocess import Popen, PIPE
from threading import Thread
from zipfile import ZipFile

from django.conf import settings
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from oioioi.contests.models import Contest, ProblemInstance, Round
from oioioi.filetracker.utils import stream_file
from oioioi.problems.models import (Problem, ProblemAttachment,
                                    ProblemPackage, ProblemStatement)
from oioioi.problems.utils import (can_admin_problem,
                                  
