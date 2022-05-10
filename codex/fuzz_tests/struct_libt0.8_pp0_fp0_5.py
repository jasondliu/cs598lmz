import _struct

from .default import StructField, DEFAULT_FIELD_TYPES
from .fields import (
    BitsField,
    BytesField,
    NullField,
    PackStructField,
    SequenceField,
    StructField,
    StructMeta,
    SwitchField,
    SwitchItem,
)
from .property import ByteOrder, Property
from .utils import (
    _infer_array_size,
    _infer_byteorder,
    _infer_field_name,
    _is_struct,
    _recursive_build,
    _validate_struct,
)


def _process_fields(
    cls,
    attrs: dict,
    ordered: bool = False,
    is_root: bool = False,
    args: list = None,
    kwargs: dict = None,
):
    """
    Process attributes and create packedbit.StructField objects using specified
    keyword arguments and attributes.

    Args:
        attrs: Attributes to be processed.

    Keyword Args:
        ordered (bool): Indicates if the
