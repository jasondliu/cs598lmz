from _struct import Struct
s = Struct.__new__(Struct)
s.new = Struct.__new__
from collections import namedtuple
from datetime import date, datetime

from dateutil.parser import parse as dateutil_parse
from dateutil.tz import tzutc
from dateutil.tz import tzoffset
from dateutil.tz import tzlocal
from dateutil.tz import tzwinlocal

from genson import SchemaBuilder
from genson.schema import Schema
from genson.errors import EnumException
from genson.utils import to_schema

from tests.base import BaseTestMixin as BTMixin
from tests.base import BaseTestCase as BTCase
from tests.base import ValidateBaseTestCase as VBTCase


class TestSchemaBuilder(BTMixin, BTCase):

    def setUp(self):
        self.sb = SchemaBuilder()
        self.sb.add_schema({})

    def assert_schema_equal(self, schema, other):
        self.assert_equal(schema.json, other.json)
