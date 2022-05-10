import mmap

from typing import Dict, Tuple

from zuper_typing import dataclass
from zuper_typing.annotations_tricks import get_ValueType
from zuper_typing.annotations_tricks import is_List
from zuper_typing.logging_tricks import indent, log_stream
from zuper_typing.my_dict import makedict
from zuper_typing.span_tricks import make_span
from zuper_typing.subscripts import make_subscripts
from zuper_typing.subobjects import MakeSubobjects
from zuper_typing.usings import inspect_usings
from zuper_typing.zip_tricks import make_zip
from zuper_typing.exceptions import ZTypeError
from zuper_typing import dataclass_to_zt
from zuper_typing.logging_tricks import log
from zuper_typing import typing_from_annotations


def make_from_annotations(annotations) -> "Type[C]:":
    dataclass_from_annot
