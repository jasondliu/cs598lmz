fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# 测试
import pytest

from problems.problem_0231 import Solution


@pytest.mark.parametrize("n, expected", [
    (1, True),
    (2, True),
    (3, False),
    (4, True),
    (5, False),
    (7, False),
    (8, True),
    (9, False),
    (10, False),
])
def test_isPowerOfTwo(n, expected):
    assert Solution().isPowerOfTwo(n) == expected
