import mmap

from ._dyn.internal import CTypesHelperMixin, PointerHelperMixin
from ._dyn.libopenmpt import libopenmpt
from ._dyn.libopenmpt import ffi
from ._dyn.libopenmpt import _ffi_api, _ffi_api_pointer
from ._dyn.libopenmpt_stream_callbacks import (
  OpenMptStreamCallbacks,
  OpenMptStreamCallbacksInstance,
)
from . import _util


class OpenMptLibraryNotFoundError(Exception):
  pass


class OpenMptLoader(CTypesHelperMixin, PointerHelperMixin):

  def __init__(self, **kwargs):
    super(OpenMptLoader, self).__init__()
    self.logging_enabled = kwargs.get("logging_enabled", False)
    self.log_level = kwargs.get("log_level", 1)
    self.log_callback = kwargs.get("log_callback", None)

  def _setup(self):
    self.open
