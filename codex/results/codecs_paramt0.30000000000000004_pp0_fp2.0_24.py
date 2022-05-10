import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import util
from . import config
from . import constants
from . import exceptions
from . import models
from . import settings
from . import signals
from . import version
from . import views

from . import http
from . import middleware
from . import wsgi
from . import routing

from . import apps
from . import cli
from . import commands
from . import extensions
from . import log
from . import mail
from . import plugins
from . import signals
from . import templates
from . import testing
from . import utils
from . import validators

from . import __main__
from . import __version__

from . import http
from . import middleware
from . import wsgi
from . import routing

from . import apps
from . import cli
from . import commands
from . import extensions
from . import log
from . import mail
from . import plugins
from . import signals
from . import templates
from . import testing
from . import utils
from . import validators

from . import __main__
