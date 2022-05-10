import mmap
import os
import re
import sys
import time
import traceback
import urllib

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.html import escape
from django.utils.translation import ugettext as _

from desktop.lib.django_util import render, render_json
from desktop.lib.exceptions_renderable import PopupException
from desktop.lib.i18n import smart_unicode
from desktop.models import Document, Document2, Document2Permission, DocumentTag, DocumentTag2, Document2Tag
from hadoop.fs.exceptions import WebHdfsException
from hadoop.fs.hadoopfs import Hdfs
from hadoop.fs.webhdfs import WebHdfs
from liboozie.oozie_api import get_oozie
from liboozie.submission2 import Submission
from liboozie.utils import model_to_dict
from
