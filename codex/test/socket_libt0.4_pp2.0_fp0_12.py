import socket

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST

from mezzanine.conf import settings
from mezzanine.generic.models import ThreadedComment
from mezzanine.generic.forms import ThreadedCommentForm
from mezzanine.utils.email import send_mail_template
from mezzanine.utils.urls import next_url
from mezzanine.utils.views import render, set_cookie
from mezzanine.blog.models import BlogPost, BlogCategory
