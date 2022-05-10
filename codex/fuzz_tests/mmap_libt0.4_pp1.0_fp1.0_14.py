import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import traceback
import urllib
import urllib2

from datetime import datetime
from wsgiref.handlers import format_date_time

from django.conf import settings
from django.core.cache import cache
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.http import http_date, parse_http_date
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache

from seaserv import seafile_api, ccnet_api
from pysearpc import SearpcError
from seaserv import seafserv_threaded_rpc, seafserv_rpc, web_get_access_token
from seahub.auth.decorators import login_required
from seahub.auth import login as auth
