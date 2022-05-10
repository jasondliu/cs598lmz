import weakref

from collections import namedtuple
from dateutil import parser as date_parser
from dateutil import tz
from sqlalchemy import MetaData, select, Table, Column, Index
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime, Integer, Unicode, VARCHAR

from core.observables import Observable
from core.errors import ObservableValidationError
from core.helpers import parse_date_to_utc
from core.spreadsheet import Spreadsheet
from api.enum import Enum
from core import role
from core.config.config import OrchestratorConfig


class TimeFrame(Enum):
    HOUR = '1 hour'
    DAY = '1 day'
    WEEK = '7 days'
    MONTH = '1 month'


class Domain(Observable):

    update = None
    report = None
    create = None
    primary_key = "domain"

