import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "hello"
    
    
def get_numpy_data(table, features, output):
    table['constant'] = 1 # adding a constant column to the data set
    # please take care of the fact that the intercept is now stored in the
    # constant column and should be wise to remove it later
    # add the column 'constant' to the front of the features list so that we
    # can extract it along with the others:
    features = ['constant'] + features # this is how we combine two lists
    # select the columns of data_SFrame given by the features list into the
    # data_SFrame_features (now including constant):
    features_table = table[features]
    # the following line will convert the features_table into a numpy matrix:
    feature_matrix = features_table.to_numpy()
    # assign the column of data_SFrame associated with the output to the
    # array output_array
    output_table = table[output]
    # the following will convert the SArray into a numpy array by first
    # converting it to a
