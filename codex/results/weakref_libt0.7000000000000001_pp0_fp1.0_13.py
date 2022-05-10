import weakref

import pytest

import aim.utils.dict as dict_utils
from aim.utils import AimDict


def test_merge_dicts():
    assert dict_utils.merge_dicts({}, {}) == {}
    assert dict_utils.merge_dicts({'a': 1}, {}) == {'a': 1}
    assert dict_utils.merge_dicts({'a': 1}, {'a': 2}) == {'a': 2}
    assert dict_utils.merge_dicts({'a': 1}, {'a': 2}, {'a': 3}) == {'a': 3}
    assert dict_utils.merge_dicts({'a': 1}, {'a': 2}, {'a': 3}) == {'a': 3}
    assert dict_utils.merge_dicts({'a': 1}, {'a': 2, 'b': 2}, {'a': 3}) == {
        'a': 3,
        'b': 2,
    }


def test_update_dict():
    assert dict_
