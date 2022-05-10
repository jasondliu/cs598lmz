import codecs
codecs.register_error('strict', codecs.ignore_errors)
import zipfile
# import Image
import struct
import os
import shutil
import urllib
import re
import sys
import unicodedata
import mimetypes

from django.db import IntegrityError
from django.utils.text import slugify
from django.core.exceptions import SuspiciousFileOperation
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import UploadedFile
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile

from mezzanine.core.fields import RichTextField
from mezzanine.core.models import SiteRelated
from mezzanine.generic.fields import CommentsField, RatingField
from mezzan
