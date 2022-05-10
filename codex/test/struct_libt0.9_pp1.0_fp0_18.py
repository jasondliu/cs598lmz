import _struct
from datetime import time, timezone, tzinfo
from .common import (
    supports_extended_time,
    TimeInfoMixin,
    GMT,
    FixedOffset,
    utc,
    test_tzoffset,
    Timezone,
    tzname_in_python2,
    USTimeZone,
)
from .sqlalchemy_test_base import SqlalchemyTestBase


sa = pytest.importorskip("sqlalchemy")
pytestmark = pytest.mark.sqlalchemy


class SQLAlchemyTestBase(SqlalchemyTestBase):
    _off_zone = FixedOffset(330, "UTC+0530", True)
    _on_zone = FixedOffset(-330, "UTC-0530", False)
    _x_zone = FixedOffset(-270, "UTC-0430")
    _zero_zone = utc

    dbapi = None

    def setup_method(self):
        if not supports_extended_time:
            pytest.skip("no support for extended time")

