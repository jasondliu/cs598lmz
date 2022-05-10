import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The following is a hack to make sure that the default encoding is UTF-8.
# This is necessary because the default encoding is ASCII on Python 2.7.
# See http://stackoverflow.com/questions/3828723/why-should-we-not-use-sys-setdefaultencodingutf-8-in-a-py-script
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import re
import subprocess
import sys
import tempfile
import time
import traceback

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.encoding import smart_unicode

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_filename

from reviewboard.diffviewer.models import DiffSet, FileDiff
