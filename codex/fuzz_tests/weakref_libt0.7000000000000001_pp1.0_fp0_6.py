import weakref

from django.conf import settings

from tower import ugettext as _

from tastypie.bundle import Bundle
from tastypie.exceptions import ApiFieldError, Unauthorized
from tastypie.utils import dict_strip_unicode_keys, get_class_name, \
    get_related_resource, to_class

# Access to a protected member _meta of a client class
# pylint: disable-msg=W0212

class ApiField(object):
    """
    An abstract field.
    """
    dehydrated_type = 'string'
    help_text = ''
    default = ''
    attribute = None
    null = False

    def __init__(self, attribute=None, default=None, null=False,
                 readonly=False, help_text=None):
        self.attribute = attribute
        self.default = default or self.default
        self.null = null
        self.readonly = readonly

        if help_text:
            self.help_text = help_text

    def _get_value(
