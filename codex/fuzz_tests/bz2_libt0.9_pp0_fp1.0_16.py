import bz2
bz2.__file__

x_train, labels_train, x_test, labels_test = helper.load_data()
# Explore the dataset
batch_id = 5
sample_id = 5
helper.display_stats(x_train, labels_train, batch_id, sample_id)
 

def normalize(x):
    """
    Normalize a list of sample image data in the range of 0 to 1
    : x: List of image data.  The image shape is (32, 32, 3)
    : return: Numpy array of normalize data
    """
    return x / 255


"""
DON'T MODIFY ANYTHING IN THIS CELL THAT IS BELOW THIS LINE
"""
tests.test_normalize(normalize)

# Preprocess all the data and save it
helper.preprocess_and_save_data(cifar10_dataset_folder_path, normalize, one_hot_encode)

import pickle
import problem_unittests as tests
import helper

# Load the Preprocessed Validation data
valid_features
