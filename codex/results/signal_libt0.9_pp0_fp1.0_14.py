import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import traceback

try:
    from trac.util.compat import set
    from trac.util.presentation import Paginator
    from trac.util.text import to_unicode, unicode_unquote
except ImportError:
    set = None
    import paginator
    Paginator = paginator.Paginator
    from presenter.util.unicode import to_unicode, unicode_unquote

from presenter.presentermap import PresentationMap
from presenter.traccgi import get_environ, get_trac_form_data, \
                              get_trac_template_data


class TracPresenter(object):
    """Custom presenter for Trac."""

    def __init__(self, environ=None, request_handler=None):
        self.environ = environ
        if self.environ is None:
            self.environ = get_environ()
        self.request_handler = request_handler
        if self.
