import codecs
codecs.register_error("surrogateescape", codecs.surrogateescape_error)

import sqlite3

# encoding: utf-8
# author: Kevin Schaul


class DataFrame(pd.DataFrame):
    """This is a custom data frame made by messing with panda's dataframe

    Args:
        data: Data to be placed in the dataframe. Can be a list, or a DataFrame,
            and can contain numpy arrays, lists, or dictionaries. In the case of
            dictionaries, the keys are used as column names.
        index: Data to be used as the index. Can be a list, or a DataFrame
        columns: Names for the columns.
    """

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            super().__init__(*args, **kwargs)
            if isinstance(args[0], type(self)):
                for column in self.columns:
                    if '_mean' in column:
                        self[column] = self[column].apply(pd.to_numeric)

