from lzma import LZMADecompressor
LZMADecompressor.__module__ = "lzma"

from typing import Any, Dict, List, Optional, Text, Union

from google.protobuf.message import DecodeError
from google.protobuf.message import Message
from google.protobuf.pyext._message import DecodeError as ProtoBufDecodeError

from rasa.nlu.constants import (
    MESSAGE_RESPONSE_ATTRIBUTE,
    REQUESTED_SLOT,
    ENTITIES,
    TEXT,
    INTENT,
    INTENT_RANKING_KEY,
    INTENT_NAME_KEY,
    ENTITY_ATTRIBUTE_ROLE,
    ENTITY_ATTRIBUTE_GROUP,
    ENTITY_ATTRIBUTE_TYPE,
    ENTITY_ATTRIBUTE_CONFIDENCE,
    ENTITY_ATTRIBUTE_START,
    ENTITY_ATTRIBUTE_END,
    ENTITY_ATTRIBUTE_VALUE,
    ENTITY_ATTRIBUTE_EXTRACTOR,
    ENTITY
