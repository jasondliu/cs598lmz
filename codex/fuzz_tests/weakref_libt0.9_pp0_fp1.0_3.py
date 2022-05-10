import weakref
from typing import *

from .design import DesignDef, DesignDefDesc, DesignDesc
from .design import DesignTool
from .entity import Entity, EntityDef, EntityDefDesc, EntityDesc
from .pattern import SelectionPattern, SelectionPatternDesc
from .utils import get_class_by_name, get_object_id, get_object_id_map
from .world import World, WorldDef, WorldDefDesc, WorldDesc

__all__ = ['examine']


def examine(obj: object) -> Optional[obj]:
    if isinstance(obj, (int, float, str)) and obj:
        return obj
    elif isinstance(obj, (tuple, list)):
        return obj
    elif isinstance(obj, dict):
        return obj

    if isinstance(obj, DesignDef):
        obj = get_design_def_desc(obj)
    elif isinstance(obj, Design):
        obj = get_design_desc(obj)
    elif isinstance(obj, DesignTool):
        obj = get_design_tool_desc(obj)
    elif
