import mmap
# Test mmap.mmap(0, 1).read_byte() == '\0'.
if(mmap.mmap(0, 1).read_byte() != '\0'):
    raise ImportError('mmap not available')

# Import all modules
from ternip.normaliser import Normaliser
from ternip.baseform import BaseformGenerator
from ternip.rule_engine.engine import RuleEngine
from ternip.document import *
from ternip.timex import Timex, timex_to_iso
from ternip.formats import *
from ternip.rule_engine.helpers import *
from ternip.utilities import *
