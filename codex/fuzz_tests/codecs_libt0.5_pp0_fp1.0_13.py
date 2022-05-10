import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.db_utils import *

from utils.utils import *
from utils.config import *

from utils.nlp.word2vec import *
from utils.nlp.stopword import *
from utils.nlp.sentence import *

from utils.nlp.preprocess import *
from utils.nlp.token import *

from utils.nlp.topic_modeling import *
from utils.nlp.topic_modeling_utils import *

from utils.nlp.embedding import *
from utils.nlp.embedding_utils import *

from utils.nlp.sentiment import *
from utils.nlp.sentiment_utils import *

from utils.nlp
