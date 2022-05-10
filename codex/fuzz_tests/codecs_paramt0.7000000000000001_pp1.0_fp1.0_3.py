import codecs
codecs.register_error('substitute_xml', substitute_xml)

import os
import re
from unittest import TestCase

from django.conf import settings
from django.core.management import call_command
from django.db.models import Q
from django.template import Template
from django.template.loaders import app_directories
from django.test import TestCase as DjangoTestCase

from cms import constants
from cms.api import create_page, create_title
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.models import Page, Title, StaticPlaceholder, PagePermission
from cms.models.placeholdermodel import Placeholder
from cms.plugin_rendering import ContentRenderer, render_placeholder
from cms.toolbar.toolbar import CMSToolbar
from cms.utils.compat import DJANGO_1_7
from cms.utils.helpers import get_cms_setting
from cms.utils.page_permissions import (
    user_can
