import codecs
codecs.register_error("strict", codecs.ignore_errors)

UNKNOWN = "_UNK_"
# stack + memory
UNKNOWN_POS = "_UNK_"
# position
NULL_POS = "_NULL_"
UNKNOWN_CHAR = "_UNK_"
NULL_CHAR = "_NULL_"
UNKNOWN_CHAR_POS = "_UNK_"
NULL_CHAR_POS = "_NULL_"
ROOT = "TOP"
NULL = "*NULL*"
ROOT_POS = "TOP"
NULL_POS = "*NULL*"
ROOT_CHAR = "TOP"
NULL_CHAR = "*NULL*"

MAX_CHAR_LENGTH = 45

UNK_IDX = 0
ROOT_IDX = 1
NULL_IDX = 2
ROOT_CHAR_IDX = 3
NULL_CHAR_IDX = 4

NUM_SYMBOLIC_TAGS = 2

PADDING_WORD = "_PAD_"
PADDING_CHAR = "_PAD_"
NUM_WORD_PADDING = 1

END = "_END_
