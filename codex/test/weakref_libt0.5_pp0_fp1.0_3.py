import weakref

from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.template import (
    engines,
    loader,
    TemplateDoesNotExist,
    TemplateSyntaxError,
)
from django.template.base import Origin
from django.template.engine import Engine
from django.utils.module_loading import import_string
from django.utils.safestring import SafeData
from django.utils.text import get_text_list
from django.utils.translation import gettext as _, pgettext

from . import settings
from .compat import is_authenticated, user_model_label
from .exceptions import TemplateResponseNotAllowed
from .utils import (
    is_html_input_type,
    is_html_output_type,
    is_json_output_type,
    is_text_input_type,
    is_text_output_type,
)

logger = logging.getLogger(__name__)
