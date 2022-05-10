import weakref
from .base import Base


logger = logging.getLogger("pytablewriter")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(stream_handler)


class _ProxyBase(Base):
    def __init__(self):
        self._writer_weakref = None

    @property
    def _writer(self):
        return self._writer_weakref()

    @property
    def _is_closed(self):
        writer = self._writer_weakref()
        if writer is None:
            raise ValueError("writer have been closed")

        return writer.is_closed

