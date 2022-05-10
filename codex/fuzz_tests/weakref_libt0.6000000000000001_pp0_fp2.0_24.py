import weakref

from sqlalchemy import Boolean, Column, Integer, String, Table, func
from sqlalchemy.orm import aliased, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy_utils import LtreeType, Ltree
from sqlalchemy_utils.functions import lquery

from . import _sqlalchemy_utils as sau

from .utils import ensure_tuple, ensure_list
from .const import (
    LANGUAGE_FORM_CHOICES,
    LANGUAGE_FORM_CHOICES_REVERSE,
    LANGUAGE_FORM_DEFAULT,
    LANGUAGE_FORM_DEFAULT_REVERSE,
    LANGUAGE_FORM_COMBINED_CHOICES,
    LANGUAGE_FORM_COMBINED_CHOICES_REVERSE,
    LANGUAGE_FORM_COMBINED_DEFAULT,
    LANGUAGE_FORM_COMBINED_DEFAULT_RE
