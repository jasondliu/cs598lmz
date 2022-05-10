import weakref

import numpy as np

from .. import ureg
from .. import Q_
from ..core import (Unit, UnitsContainer, UnitsContainerOperator,
                    get_current_magnitude,
                    get_current_units, get_converter,
                    get_current_mksa_unit,
                    get_current_context,
                    get_current_dimensionality,
                    is_dimensionless,
                    set_enabled_contexts,
                    set_enabled_dimensions,
                    set_enabled_units,
                    get_dimensionality,
                    set_application_registry,
                    set_context,
                    set_current_magnitude,
                    set_current_units,
                    set_converter,
                    set_current_mksa_unit,
                    set_current_context,
                    set_current_dimensionality,
                    set_dimensionality,
                    set_root_units,
                    set_root_context,
                    set_root_preferences,
                    set_root_registries,
                    set_root_system,
                    set_root_
