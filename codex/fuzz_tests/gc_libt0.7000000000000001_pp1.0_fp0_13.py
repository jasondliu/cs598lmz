import gc, weakref
import logging
from . import errno
from .utils import wrap_exceptions, run_in_threadpool

from .stream import Stream, _DEFAULT_LIMIT
from .h2.connection import H2Connection as Connection
from .h2.errors import ProtocolError, NoAvailableStreamError, H2Error
from .h2.exceptions import (
    ProtocolError as H2ProtocolError,
    StreamClosedError as H2StreamClosedError,
    TooManyStreamsError as H2TooManyStreamsError,
    FrameTooLargeError as H2FrameTooLargeError,
    UpgradeError as H2UpgradeError,
    InvalidPseudoHeaderError as H2InvalidPseudoHeaderError,
    InvalidHeaderError as H2InvalidHeaderError,
    InvalidProtocolVersionError as H2InvalidProtocolVersionError,
    TooManyHeadersError as H2TooManyHeadersError,
    MissingSettingsFrameError as H2MissingSettingsFrameError,
    FlowControlError as H2FlowControlError,
    StreamIDTooLowError as H2StreamIDTooLowError,
    InvalidWindow
