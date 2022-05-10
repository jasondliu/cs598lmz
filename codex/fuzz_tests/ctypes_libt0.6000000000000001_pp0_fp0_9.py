import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello, World!", "Your title", 1)

#------------------------------------------------------------------------------
# HELPER FUNCTIONS
#------------------------------------------------------------------------------
def get_missing_value_index(dataframe):
    """
    :param dataframe:
    :return:
    """
    print("Determine which columns have missing values")
    missing_value_index = [i for i, v in enumerate(dataframe.isnull().any()) if v]
    print("There are %i columns with missing values" % len(missing_value_index))
    return missing_value_index

def get_all_columns_in_dataframe(dataframe):
    """
    :param dataframe:
    :return:
    """
    print("Determine which columns have missing values")
    columns_list = [i for i in enumerate(dataframe.columns)]
    print("There are %i columns in this dataframe" % len(columns_list))
    return columns_list

def get_missing_value_columns(dataframe):

