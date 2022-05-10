import weakref
from collections import OrderedDict

from ..lexicon import Lexicon
from ..tokens import Token, TokenSet
from ..tokens import EOF, EOS, ErrorToken
from ..tokens import SpaceToken, NewlineToken, IndentToken, DedentToken
from ..tokens import CommentToken, CommentBlockToken
from ..states import State
from ..states import StateSet
from ..rules import Rule
from ..rules import RuleSet
from .base import Error
from .base import TokenizerBase
from .base import FLAG_TOKEN_DELIMITER, FLAG_TOKEN_EMITTER, FLAG_TOKEN_EMITTER_ARGS, FLAG_TOKEN_EMITTER_KWARGS
from .base import FLAG_TOKEN_NEWLINE_EMITTER, FLAG_TOKEN_NEWLINE_EMITTER_ARGS, FLAG_TOKEN_NEWLINE_EMITTER_KWARGS
from .base import FLAG_TOKEN_SPACE_EMITTER, FLAG_TOKEN_SPACE_EMITTER_ARGS, FL
