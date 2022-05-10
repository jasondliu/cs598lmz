import codecs
codecs.register_error('ignore', codecs.ignore_errors)

from xlrd.xldate import xldate_as_tuple

from django.db.models import Q
from django.db import transaction
from django.contrib.auth.models import User
from django.db.models.loading import get_model
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from import_export.formats.base_formats import DEFAULT_FORMATS
from import_export.results import Error, RowResult
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field
from import_export.resources import modelresource_factory
from import_export import resources

from .forms import ConfirmImportForm
from .conf import settings as import_export_settings
from .results import Result


class InvalidDataError(Exception):
    pass


class ImportMixin(object):

    def get_
