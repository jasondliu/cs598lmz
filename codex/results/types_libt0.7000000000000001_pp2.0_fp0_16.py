import types
types.FunctionType = types.LambdaType

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from django.db.models import Count
from django.utils.html import escape
from itertools import chain

from survey.models import *
from survey.forms import *
from survey.serializers import *

