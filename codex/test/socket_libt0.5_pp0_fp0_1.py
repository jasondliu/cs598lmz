import socket
import threading
import time
import datetime
import sys
import codecs
import os
import struct
import base64
import hashlib
import json
import logging
import logging.config
import traceback
import redis

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
