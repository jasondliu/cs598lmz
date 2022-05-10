import ctypes
# Test ctypes.CField2Set()
try:
    from ctypes import CField2Set
except AttributeError:
    print("CField2Set() is not defined")

# Test DataGenerator __init__()
try:
    from DataGenerator import DataGenerator
except ImportError:
    print("DataGenerator() is not defined")

# Test DataGenerator.create_data()
try:
    from DataGenerator import DataGenerator
    from pandas import get_dummies
except ImportError:
    print("DataGenerator.create_data() is not defined")
    
# Test TestClassifier.py
try:
    from TestClassifier import TestClassifier
except ImportError:
    print("TestClassifier() is not defined")

# Test TestClassifier.py
try:
    from ClassifierClass import ClassifierClass
except ImportError:
    print("ClassifierClass() is not defined")

# Test plot_classifier_results()
try:
    from plot_classifier_results import plot_classifier_results
except ImportError:
    print("plot_classifier_results
