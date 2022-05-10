import codecs
codecs.register_error('ignore', codecs.ignore_errors)

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

from django.utils.translation import ugettext as _

from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
from django.forms
