import weakref

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db import models
from django.db.models.fields import FieldDoesNotExist
from django.db.models.fields.related import \
    ForeignObjectRel, OneToOneRel, ManyToManyRel, ManyToOneRel
from django.forms.models import model_to_dict
from django.utils.translation import ugettext_lazy as _

from oscar.apps.dashboard.reports.utils import GeneratorRepository
from oscar.core.compat import AUTH_USER_MODEL
from oscar.core.loading import get_class
from oscar.models.fields import AutoSlugField
from oscar.models.fields.autoslug import slugify

ReportForm, GeneratorRepository = get_class(
    'dashboard.reports.forms', ['ReportForm', 'GeneratorRepository'])

