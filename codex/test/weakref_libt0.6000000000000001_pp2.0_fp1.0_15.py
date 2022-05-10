import weakref
from . import utils
import copy

_logger = logging.getLogger(__name__)


class QWebElement(object):
    def __init__(self, parent, we_id):
        self._parent = parent
        self._we_id = we_id

    def _js_eval(self, js):
        return self._parent._js_eval(js, self)

    def _js_eval_async(self, js):
        return self._parent._js_eval_async(js, self)

    def _js_exec(self, js):
        return self._parent._js_exec(js, self)

