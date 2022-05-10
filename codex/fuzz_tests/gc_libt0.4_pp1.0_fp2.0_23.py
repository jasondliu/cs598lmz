import gc, weakref

from . import defaults, errors, utils
from .log import log
from .utils import (
    _get_boto_session,
    _get_client_args,
    _get_client_kwargs,
    _get_client_kwargs_from_parsed_globals,
    _get_client_kwargs_from_parsed_globals_with_overrides,
    _get_endpoint_url,
    _get_event_name,
    _get_event_stream_args,
    _get_event_stream_kwargs,
    _get_event_stream_kwargs_from_parsed_globals,
    _get_event_stream_kwargs_from_parsed_globals_with_overrides,
    _get_event_stream_output_shape_name,
    _get_event_stream_output_shape_type,
    _get_event_stream_shape_name,
    _get_event_stream_shape_type,
    _get_event_stream_
