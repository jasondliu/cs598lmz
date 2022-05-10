import weakref
from datetime import datetime
from decimal import Decimal
from functools import wraps
from inspect import getcallargs
from itertools import chain
from operator import itemgetter
from typing import Any, AnyStr, Callable, Dict, Mapping, Optional, Sequence, Type, TypeVar, Union
from uuid import uuid4

import pytz
from flask import _app_ctx_stack, _request_ctx_stack
from flask import current_app, has_app_context, request
from flask.signals import Namespace
from flask_babel import get_locale
from sqlalchemy import and_, or_
from sqlalchemy.orm import Query
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import func

from abilian.core.entities import Entity, EntityQueryMixin
from abilian.core.extensions import db
from abilian.core.models.subjects import User
from abilian.core.util import utcnow
from abilian.i18n import _l
from abilian.services.audit.models import AuditEntry

