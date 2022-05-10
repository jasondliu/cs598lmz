import gc, weakref
from six.moves import range

from collections import deque
from collections import defaultdict

from ..utils import to_list, inject_all_as_keywords
from .token import Token
from .attention import Attention
from .row_choice import RowChoice
from .rule import Rule
from .word_choice import WordChoice
from .lookahead import Lookahead
from .lookbehind import Lookbehind
from .lookaround import Lookaround
from .branch import Branch
from .capturing import Capture
from .counting import Counter
from .repeating import ZeroOrMore, OneOrMore, Optional, Repeat
from .transforming import Transform, MatchFirst
from .condition import Condition, PositiveLookahead, NegativeLookahead
from ..match import Match
from ..parser import Parser
from ..pattern_utils import is_re, is_str, is_tuple, is_seq
from ..exceptions import GrammarError, GrammarWarning
from ..exceptions import IncompleteParseError, MultipleMatchesError
from ..exceptions import WrongArgumentDefOrderError
from ..pattern_utils import is_callable, is_function

