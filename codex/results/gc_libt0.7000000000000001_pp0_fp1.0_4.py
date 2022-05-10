import gc, weakref
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy.orm.collections import InstrumentedList, InstrumentedDict

from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy.dialects.postgresql import JSON as Postgres_JSON
import json
from sqlalchemy import types

from sqlalchemy.sql.expression import cast

import logging
log = logging.getLogger("DB_MODEL")
log.setLevel(logging.DEBUG)

from datetime import datetime, timedelta

from .. import settings

from ..util import jsondump
from ..util import jsonload
from ..util import jsonpickle
from ..util import jsonunpickle
from ..util import csvpickle
from ..util import csv
