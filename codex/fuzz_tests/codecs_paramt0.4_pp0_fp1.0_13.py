import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__

try:
    from . import _version
except ImportError:
    _version = None

if _version:
    __version__ = _version.get_versions()['version']

from . import settings
from . import utils
from . import exceptions
from . import models
from . import managers
from . import fields

from . import backends
from . import signals

from . import middleware

from . import decorators
from . import views

from . import admin
from . import forms

from . import urls

from . import tests

from . import management
from . import management.commands

from . import contrib

from . import conf
from . import conf.global_settings

from . import template
from . import template.defaultfilters
from . import template.defaulttags
from . import template.loaders
from . import template.context_processors

from . import contrib.auth
from . import contrib.auth.models
from . import contrib.auth.views
