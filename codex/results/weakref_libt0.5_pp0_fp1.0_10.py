import weakref
import re
from time import time

from sqlalchemy import event, inspect
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, \
    Index, Unicode, UnicodeText, Boolean, DateTime, Float, Text, or_, \
    and_, desc, asc
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm.exc import FlushError, NoResultFound
from sqlalchemy.orm.session import object_session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy.dialects.postgresql import UUID, ARRAY

from . import Base, Core, DBSession, UUIDType
from .mixins import (
    IdMixin,
    TimestampMixin,
    Annot
