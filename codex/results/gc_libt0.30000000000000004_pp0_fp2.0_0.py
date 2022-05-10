import gc, weakref
import logging
from collections import defaultdict
from itertools import chain
from functools import partial
from operator import itemgetter

from . import util
from .util import (
    _mutable_default_dict,
    _get_attr_as_list,
    _get_cls_attr_as_list,
    _is_mapped_class,
    _is_aliased_class,
    _is_mapper,
    _class_to_mapper,
    _orm_descriptor,
    _state_has_identity,
    _state_mapper,
    _state_class_key,
    _state_class_mapper,
    _state_unmodified,
    _state_dict,
    _state_active_history,
    _state_instance_dict,
    _state_session_id,
    _state_load_options,
    _state_key_token,
    _state_identity_token,
    _state_committed_state,
    _state_deleted,
    _state_p
