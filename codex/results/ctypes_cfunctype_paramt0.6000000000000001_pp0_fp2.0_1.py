import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_voidp, ctypes.c_voidp)

from . import _otf2

from . import _otf2_globals
from . import _otf2_definitions
from . import _otf2_events
from . import _otf2_events_unknown
from . import _otf2_events_mpi
from . import _otf2_events_openmp
from . import _otf2_events_threads
from . import _otf2_events_cuda
from . import _otf2_events_metric


class OTF2_EvtReaderCallbacks_struct(ctypes.Structure):
    _fields_ = [("otf2_evt_reader_callback_unknown", FUNTYPE),
                ("otf2_evt_reader_callback_buffer_flush", FUNTYPE),
                ("otf2_evt_reader_callback_measurement_on_off", FUNTYPE),
                ("otf2_evt_reader_callback_enter", FUNTYPE),
                ("otf2_evt
