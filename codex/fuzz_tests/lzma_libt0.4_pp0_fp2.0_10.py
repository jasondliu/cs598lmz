import lzma
lzma_decompress = lzma.LZMADecompressor().decompress

from . import util
from . import _compat as six

from . import _util
from ._util import (
    _read_chunks,
    _write_chunks,
    _copy_chunks,
    _copy_chunks_with_progress,
    _copy_chunks_with_progress_and_cancel,
    _copy_chunks_with_progress_and_cancel_and_pause,
    _copy_chunks_with_progress_and_cancel_and_pause_and_resume,
    _copy_chunks_with_progress_and_cancel_and_pause_and_resume_and_skip,
    _copy_chunks_with_progress_and_cancel_and_pause_and_resume_and_skip_and_throttle,
    _copy_chunks_with_progress_and_cancel_and_pause_and_resume_and_skip_and_throttle_and_retry,

