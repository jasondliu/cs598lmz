import mmap
import os
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
import zipfile
import zlib

from collections import defaultdict
from collections import namedtuple
from copy import copy
from datetime import datetime
from hashlib import md5, sha1
from operator import attrgetter
from StringIO import StringIO
from urllib import quote, unquote

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.files.storage import default_storage as storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.db import models, connection
from django.db.models import Count, Q, F
from django.db.utils import IntegrityError
from django.utils.encoding import smart_str
from django.utils.functional import cached_property
from django.utils.http import urlquote
from django.utils
