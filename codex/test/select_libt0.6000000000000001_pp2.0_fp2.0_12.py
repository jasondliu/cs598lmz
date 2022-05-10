import selectors

from . import config
from . import util


def _select_write_callback(selector, key, mask):
    """Callback for writes."""
    # From PEP 3156, this is a write callback.
    # See: https://www.python.org/dev/peps/pep-3156/#the-write-callbacks
    assert mask & selectors.EVENT_WRITE
    # The write callbacks are responsible for setting the read callback.
    selector.modify(
        key.fileobj, selectors.EVENT_READ | selectors.EVENT_WRITE,
    )


def _select_read_callback(selector, key, mask):
    """Callback for reads."""
    # From PEP 3156, this is a read callback.
    # See: https://www.python.org/dev/peps/pep-3156/#the-read-callbacks
    assert mask & selectors.EVENT_READ
    conn = key.fileobj
