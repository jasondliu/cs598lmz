import weakref
from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import Optional
from typing import Type
from typing import TYPE_CHECKING
from typing import Union
from urllib.parse import urljoin
from warnings import warn

import numpy as np
import pandas as pd
from packaging import version
from xarray import DataArray

from ..core import CookieManager
from ..core.utils import Logger
from ..core.utils import StrEnum
from ..core.utils import Timer
from ..handler import FileHandlersManager
from ..series.core import is_dataset_like
from ..series.core import is_series_like
from .decorators import SettingsDecorator
from .settings import Settings

if TYPE_CHECKING:
    from .utils import TempFileCache
    from .utils import TempFolderCache

