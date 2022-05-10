import codecs
codecs.register_error('strict', codecs.ignore_errors)

from pprint import pprint

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import escape
from django.utils.translation import ugettext as _

from oioioi.base.utils import jsonify
from oioioi.base.utils.redirect import safe_redirect
from oioioi.contests.controllers import submission_template_
