import threading
threading.stack_size(2**27)
import sys
import glob
import pickle
import os

from matplotlib import pyplot as plt

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'salary', 'bonus', 'total_stock_value', 'exercised_stock_options', 'total_payments', 'total_stock_value', 'expenses', 'other', 'from_poi_to_this_person', 'from_this_person_to_poi', 'shared_receipt_with_poi', 'restricted_stock'] # You will need to use more features

### Load the dictionary
