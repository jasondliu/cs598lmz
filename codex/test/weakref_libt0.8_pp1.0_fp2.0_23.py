import weakref

from sqlalchemy.orm import joinedload

from ichnaea.api.locate.schema import ReportSchema, ScoreSchema
from ichnaea.api.locate.source import (
    PositionSource,
    RegionSource,
    Source,
    ScoreSource,
)
from ichnaea.api.locate.query import (
    ReportPositionQuery,
    RegionQuery,
    ScoreQuery,
)
from ichnaea.constants import DEGREE_DECIMAL_PLACES
from ichnaea.geocalc import (
    distance,
    distance_accuracy,
    distance_delta,
    location_is_valid,
)
from ichnaea.heka_logging import RAVEN_ERROR
from ichnaea.models import (
    CellArea,
    CellAreaOCID,
    CellShard,
    CellShardOCID,
    OCID_MIN_ACCURACY,
    Radio,
    Score,
    WifiShard,
)
