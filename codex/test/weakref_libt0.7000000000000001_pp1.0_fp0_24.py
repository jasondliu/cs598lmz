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


