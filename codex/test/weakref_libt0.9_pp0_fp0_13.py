import weakref
from functools import cmp_to_key

from jinja2.utils import Markup, escape
from formencode import Invalid


from formalchemy.fields import null_renderer, null_validator, convert, default_required_validator, default_renderer, include_validator
from formalchemy.exceptions import ValidationFailure, _DoesNotMatch, FieldBuilderError
from formalchemy import config
from formalchemy import sorting


__all__ = ['Field']


_ = lambda x: x


class Field(object):
    """
    Field abstraction for building forms and tables.
    """

    name = None
    renderer = None
    validator = None
    required_validator = None
    inline = None
    readonly = False
    _value = None
    _key = '.'.join
    _session = None
