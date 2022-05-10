import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create an NSDictionary from a Python dictionary
def dict_to_nsdictionary(py_dict):
	return Foundation.NSDictionary.dictionaryWithDictionary_(py_dict)

# Create a Python dictionary from an NSDictionary
def nsdictionary_to_dict(ns_dict):
	return dict(ns_dict)

# Create an NSMutableDictionary from a Python dictionary
def dict_to_nsmutabledictionary(py_dict):
	return Foundation.NSMutableDictionary.dictionaryWithDictionary_(py_dict)

# Create a Python dictionary from an NSMutableDictionary
def nsmutabledictionary_to_dict(ns_dict):
	return dict(ns_dict)

# Create an NSArray from a Python list
def list_to_nsarray(py_list):
	return Foundation.NSArray.arrayWithArray_(py_list)

# Create a Python list from an NSArray
