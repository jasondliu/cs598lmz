import lzma
lzma.LZMAError

import pytest

from .. import lzmaffi


@pytest.mark.parametrize(
    'in_data',
    [
        b'',
        b'a',
        b'ab',
        b'abc',
        b'abcd',
        b'abcde',
        b'abcdef',
        b'abcdefg',
        b'abcdefgh',
        b'abcdefghi',
        b'abcdefghij',
        b'abcdefghijk',
        b'abcdefghijkl',
        b'abcdefghijklm',
        b'abcdefghijklmn',
        b'abcdefghijklmno',
        b'abcdefghijklmnop',
        b'abcdefghijklmnopq',
        b'abcdefghijklmnopqr',
        b'abcdefghijklmnopqrs',
        b'abcdefghijklmnopqrst',
        b'abcdefghijklmnopq
