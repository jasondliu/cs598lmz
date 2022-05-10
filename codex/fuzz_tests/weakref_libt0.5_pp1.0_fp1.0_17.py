import weakref

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from .. import logger
from ..core import core
from ..core.core import Core
from ..core.core import CoreError
from ..core.core import CoreInfo
from ..core.core import CoreType
from ..core.core import CoreTypeGroup
from ..core.core import get_core_info
from ..core.core import get_core_type
from ..core.core import get_core_type_group
from ..core.core import get_core_types
from ..core.core import get_core_types_by_group
from ..core.core import get_core_types_by_group_id
from ..core.core import get_core_types_by_group_name
from ..core.core import get_core_types_by_id
from ..core.core import get_core_types_by_name
from ..core.core import get_core_types_by_path
from ..core.core import get_core_types_by_path_and_name
from ..core
