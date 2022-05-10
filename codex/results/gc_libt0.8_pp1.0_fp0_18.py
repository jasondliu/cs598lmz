import gc, weakref

from dramatis.error import name_error
from dramatis.runtime import Runtime

from dramatis.actor.proxy import Proxy
from dramatis.actor.null import Null

from dramatis import release
from dramatis.future import Future, Promise, register_future
from dramatis.future.future import _make_future_result

from dramatis.exception import *
from dramatis.runtime.runtime import _actor_call_result_type
from dramatis import actor
from dramatis.actor.actor import _unwrap_actor, _unwrap_actor_or_future
from dramatis.actor.actor import _unwrap_actor_or_future_or_nil

from dramatis.actor.behavior import _am_behavior, Behavior
from dramatis.runtime.runtime import Cont
#from dramatis.runtime.runtime import _actor_yield_result_type

from dramatis.exceptions import DramatisError
from dramatis.runtime.runtime import _Actor

class _ActorLogic(object):

    class Context(object):
        def __init__(self,logic):
            self
