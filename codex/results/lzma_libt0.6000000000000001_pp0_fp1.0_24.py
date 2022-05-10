import lzma
lzma.open

from pyminifier.minification import minify

from io import StringIO

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.template.defaultfilters import slugify
from django.db.models import Q

from .models import *
from .forms import *
from .filters import *
from .tokens import account_activation_
