import gc, weakref

from werkzeug.exceptions import NotFound
from werkzeug.wrappers import Request
from werkzeug.serving import run_simple
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.routing import Map, Rule
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader

from uliweb import application
from uliweb.utils.common import import_attr
from uliweb.utils.pyini import Ini
from uliweb.core import Container
from uliweb.core.SimpleFrame import Request as Request_
from uliweb.core.template import render_template_to_string
from uliweb.core.html import build_html, begin_tag, end_tag, begin_end_tag
from uliweb.core.commands import CommandManager
from uliweb.core.SimpleFrame import Uliweb as Uliweb_
from uliweb.core.commands import CommandError, gettext_lazy as _
from uliweb.core.template import template_extensions

