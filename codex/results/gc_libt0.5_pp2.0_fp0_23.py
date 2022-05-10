import gc, weakref
import numpy as np
import pandas as pd
import pytest

from . import util


class TestDataFrame:

    def test_dataframe_constructor(self):
        df = pd.DataFrame()
        assert len(df) == 0

        df = pd.DataFrame(index=range(5))
        assert len(df) == 5

        df = pd.DataFrame(columns=range(5))
        assert len(df.columns) == 5

        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        assert len(df) == 3

        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=range(3))
        assert len(df) == 3

        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]},
                          index=pd.Index(range(3), name='idx'))
        assert
