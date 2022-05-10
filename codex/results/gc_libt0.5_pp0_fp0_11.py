import gc, weakref
from collections import defaultdict
from itertools import chain
import logging

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
from django.utils.encoding import force_unicode
from django.utils.functional import lazy
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.db.models.fields import FieldDoesNotExist
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib.admin.util import lookup_needs_distinct, prepare_lookup_value
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import capfirst
from django.
