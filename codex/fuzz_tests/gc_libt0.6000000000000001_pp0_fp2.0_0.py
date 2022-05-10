import gc, weakref, logging

from . import luabind
from . import luabind_types as lua

log = logging.getLogger(__name__)

_map_refs = weakref.WeakKeyDictionary()

def _map_key_to_ref(key):
    try:
        return _map_refs[key]
    except KeyError:
        ref = weakref.ref(key)
        _map_refs[key] = ref
        return ref

def _map_key_from_ref(ref):
    return ref()

def _map_key_from_lua(ref):
    return _map_key_from_ref(lua.luaX_to_object(ref))

def _map_key_to_lua(key):
    ref = _map_key_to_ref(key)
    return lua.luaX_to_object(ref)

class Map(object):
    """A mapping of keys to values."""

    _map_type = lua.lua_State.registry_ref_map_
