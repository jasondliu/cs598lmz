import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.conf import settings
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from django.utils.translation import ungettext
from django.utils.translation import get_language
from django.utils.translation import activate
from django.utils.translation import to_locale
from django.utils.translation import get_language_info
from django.utils.translation import check_for_language
from django.utils.translation import get_language_from_request
from django.utils.translation import get_language_from_path
from django.utils.translation import ngettext
from django.utils.translation import gettext
from django.utils.translation import pgettext
from django.utils.translation import npgettext
from django.utils.translation import string_concat
from django.utils.translation import gettext_noop
from django.utils.translation import gettext_l
