import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.settings import api_settings
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
from django.conf import settings

