import weakref

import abc
import six
from typing import Any, Set, Callable, List, Mapping, Tuple, Type, Union

from anki.collection import _Collection
from anki.lang import _, ngettext
from anki.utils import intTime, splitFields

from aqt.utils import (
    TR,
)
from aqt.utils import showWarning as showWarning

from .consts import MODEL_CLOZE, HOOK_ADD_CARDS, HOOK_ADD_NOTE_FACTS, REVLOG_ADDED
from .main import AnkiWebView
from .models import AddModel
from .notes import FactPrototype
from .notes import FactPrototypeSelector
from .notes import FactPrototypeValidator
from .notes import NotePrototype
from .notes import NotePrototypeValidator
from .notes import TagAwareValidator
from .utils import edit_current
from .widgets.dialogs import get_tags_from_note_info
from .widgets.shortcuts import add_warning_defaults
from .widgets.shortcuts import show_
