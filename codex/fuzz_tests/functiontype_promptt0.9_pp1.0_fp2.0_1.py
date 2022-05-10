import types
# Test types.FunctionType/types.CodeType/types.FrameType

class TestFCTypes():

    def test_add(self):
        df['c'] = df.apply(lambda row: row.a + row.b, axis=1)
        expected = df.a.add(df.b)
        tm.assert_series_equal(df['c'], expected)

    def test_custom_add(self):
        self.df['c'] = self.df.apply(lambda row: row.a.add(row.b), axis=1)
        result = self.df.a + self.df.b
        tm.assert_series_equal(self.df['c'], result)

        df = DataFrame({'a': [1.1, 2.1, 3.1],
                        'b': [1, 2, 3],
                        'c': np.array(2, dtype=object),
                        'd': np.array(5, dtype=object),
                        'e': np.array(5, dtype=object)})

        df['d'] = df
