import weakref
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.views import generic
from django.utils.prefetching import Prefetch
from django.utils.datastructures import SortedDict, MultiValueDict, MergeDict
from django.utils.translation import ugettext as _
from django.utils.decorators import classonlymethod
from django.utils.functional import curry
from django.http import Http404, QueryDict
from decimal import Decimal
from copy import deepcopy
# URL creation
from django.core.urlresolvers import NoReverseMatch, reverse
from django.http import HttpResponseRedirect
from django.utils.http import urlencode
# Caching
from django.views.decorators.cache import never_cache
