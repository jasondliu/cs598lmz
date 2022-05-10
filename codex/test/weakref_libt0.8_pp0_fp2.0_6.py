import weakref

from RO.Astro import llv
from RO.StringUtil import strFromException

from .base_actor import BaseActor, KeyVarDispatcher

# special sentinel value that indicates what happens
# if a variable is updated but the value has not changed
# - None: no change
# - True: send an update
# - False: do not send an update
ChangePolicy = enum.Enum(
    "ChangePolicy",
    "Unchanged True False",
    start=0,
)

__all__ = ["KeyVarActor"]

class KeyVarActor(BaseActor):
    """
    Key variable actor.
    
    Calls user-supplied callbacks when key variables change.
    """
