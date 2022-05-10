import types
types.FunctionType = types.BuiltinFunctionType
from functools import partial
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.cache import cache
from django.db.models.query_utils import Q
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
