from bz2 import BZ2Decompressor
BZ2Decompressor()

from gzip import GzipFile
GzipFile

from zlib import decompress
decompress

# prompt-toolkit
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
AutoSuggestFromHistory

from prompt_toolkit.application import get_app
get_app

from prompt_toolkit.buffer import Buffer
Buffer

from prompt_toolkit.document import Document
Document

from prompt_toolkit.enums import EditingMode
EditingMode

from prompt_toolkit.filters import has_focus, Condition
has_focus, Condition

from prompt_toolkit.formatted_text import PygmentsTokens
PygmentsTokens

from prompt_toolkit.history import FileHistory
FileHistory

from prompt_toolkit.key_binding.bindings.focus import FocusNext, FocusPrevious
FocusNext, FocusPrevious

from prompt_toolkit.key_binding.vi_state import InputMode
InputMode

from prompt_toolkit.layout.containers import (
    Window, FloatContainer, HSplit, VSplit, WindowAlign, Float, FloatDim
