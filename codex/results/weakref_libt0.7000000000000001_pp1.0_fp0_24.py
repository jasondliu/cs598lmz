import weakref

from pygments import highlight
from pygments import lexers
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.lexers import get_lexer_by_mimetype
from pygments.lexers import guess_lexer
from pygments.lexers import guess_lexer_for_filename
from pygments.util import ClassNotFound
from requests import Session

from . import exceptions
from . import utils


logger = logging.getLogger(__name__)


class PygmentsRenderer(object):
    """
    The Pygments renderer is responsible for transforming source code into
    highlighted HTML.

    It can either be used directly or as a callback for the :class:`~.GitLabClient`.

    :param str style: The Pygments style to use. Defaults to "monokai".
    :param str css_class: The HTML class that should be given to the `<pre>`
                          element. Defaults to "highlight".
    :param bool full: Whether
