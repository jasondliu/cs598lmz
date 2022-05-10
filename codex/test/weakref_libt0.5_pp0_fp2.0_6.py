import weakref

import numpy as np
import pytest

import pandas as pd
from pandas import DataFrame, Index, MultiIndex, Series
import pandas._testing as tm


class TestDataFrameGet:
    def test_getitem_pop_frame(self):
        df = DataFrame(np.random.randn(10, 4), columns=list("ABCD"))
        A = df.pop("A")
        tm.assert_series_equal(A, df["A"])

        with pytest.raises(KeyError, match=r"^'A'$"):
            df["A"]

    def test_getitem_slice_integers(self):
        # GH#1041
        df = DataFrame(np.random.randn(10, 4), columns=list("ABCD"))
        result = df.iloc[:, :2]
        expected = df.reindex(columns=["A", "B"])
        tm.assert_frame_equal(result, expected)

