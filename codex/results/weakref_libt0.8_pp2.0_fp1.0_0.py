import weakref
from django.core.signing import TimestampSigner
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.views.generic import View
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.urls import reverse_lazy

from .models import (
    Project, ProjectData, Component, ComponentData,
    ComponentField, ComponentDataField,
    FieldItem, FieldItemData, FieldItemValue,
    ContainerFieldItemData,
)
from .forms import DataFieldFileForm
from .utils import (
    FullscreenDataViewMixin,
    get_field_for_field_item,
    get_data_for_field_item,
