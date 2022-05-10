from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor # re-assign, if it's not used, pyflakes.

from xblock.core import XBlock
from xblock.fields import Scope, ScopeIds, String, Boolean, Integer, Float, List, Dict
from xblock.fragment import Fragment
from xblock.validation import Validation
from xblock.exceptions import JsonHandlerError, NoSuchViewError
from xblock.runtime import KvsFieldData, DictKeyValueStore
from xblock.fields import Dict
from xblock.reference.user_service import XBlockUser
from xblock.reference.plugins import Plugin
from xblock.reference.runtime import IdReader, IdGenerator
import inspect
import json
import traceback
import sys

from xblock_django.models import XBlockState
from xblockutils.studio_editable import StudioEditableXBlockMixin

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.test.utils import override_settings
from django.conf import settings
from free
