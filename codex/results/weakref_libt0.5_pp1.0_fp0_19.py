import weakref
from datetime import datetime
from functools import partial
from operator import itemgetter
from itertools import chain, groupby, product
from collections import namedtuple, defaultdict
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm import class_mapper
from sqlalchemy.sql.expression import cast, func, select, and_, or_, case, literal_column
from sqlalchemy.types import Integer, Numeric, DateTime, String, Boolean, Float
from sqlalchemy import text
from sqlalchemy.sql.functions import coalesce, now

from trytond.model import (
    ModelView, ModelSQL, ModelSingleton, fields, Unique, sequence_ordered)
from trytond.wizard import Wizard, StateView, StateTransition, StateAction, \
    Button
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval, If, Bool, PYSONEncoder, Date
from trytond.tools import reduce_ids, grouped_slice

