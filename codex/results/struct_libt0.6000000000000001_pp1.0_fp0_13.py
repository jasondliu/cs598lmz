import _struct

import pytest

from .. import _struct_as_dict
from .. import _struct_as_dict_ordered
from .. import _struct_as_dict_ordered_with_values
from .. import _struct_as_dict_with_values
from .. import _struct_as_json
from .. import _struct_as_json_ordered
from .. import _struct_as_json_ordered_with_values
from .. import _struct_as_json_with_values


def test_struct_as_dict_with_values():
    struct = _struct.Struct('i?f')
    struct.pack(1, True, 3.14)
    assert _struct_as_dict_with_values(struct) == {
        'format': 'i?f',
        'size': struct.size,
        'values': (1, True, 3.14),
    }


def test_struct_as_dict_ordered_with_values():
    struct = _struct.Struct('i?f')
    struct.pack(1, True, 3.14)
    assert _struct
