import codecs
# Test codecs.register_error first
# so that exceptions can be imported if necessary.
codecs.register_error('test', codecs.strict_errors)

from django.conf import settings as real_settings
from django.template import TemplateDoesNotExist
from django.utils import translation
from django.utils.translation import check_for_language, get_language_from_request
from django.utils.log import getLogger
from django.utils.functional import lazy


from django.utils.translation.trans_real import to_language

from django.utils.functional import lazy as lazy_func

from modeltranslation import settings as mt_settings
from modeltranslation.utils import remove_trailing_garbage
from modeltranslation.utils import build_localized_fieldname as blf
from modeltranslation.utils import get_translation_fields as gtf
from modeltranslation.utils import (
    get_language, get_real_fieldname, get_default_language,
    is_default_language, deactivate_all, build_localized_fieldname)
