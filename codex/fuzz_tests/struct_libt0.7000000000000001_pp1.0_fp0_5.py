import _struct

from typing import (
    Any,
    BinaryIO,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

from . import (
    BINARY_CHUNK_TYPE,
    BINARY_BLOCK_TYPE,
    BINARY_FILE_HEADER,
    BINARY_VERSION,
    BINARY_VERSION_MAX,
    BINARY_VERSION_MIN,
    BINARY_FILE_FOOTER,

    BASE_TYPES,
    BASIC_TYPES,
    EXTENDED_TYPES,
    TYPE_LENGTHS,

    BLOCK_TYPE_NONE,
    BLOCK_TYPE_ARRAY,
    BLOCK_TYPE_COMPOUND,

    CHUNK_TYPE_END,
    CHUNK_TYPE_HEADER,
    CHUNK_TYPE_DATA,
    CHUNK_TYPE_FOOTER,
)

from .nbt import (
    TAG_
