import weakref
import threading

#
# Base class for detecting the string status of an item
#

class StringStatus(object):
    def __init__(self, resultManipulator):
        self.resultManipulator = resultManipulator

    def is_string(self):
        raise NotImplementedException("Subclass must implement this method")

    def _parallel_status(self):
        is_collection = self.is_collection()
        if is_collection == True:
            return 'Collection'
        elif is_collection == False:
            return 'NotCollection'
        else:
            return None

    def _is_string_collection(self, data):
        if not self.is_collection(data):
            return False

        length = self.resultManipulator.sequence_length_py(data)
        if length == 0:
            return False

        status = self.resultManipulator.first_element_string_status_py(data, 0)
        return status['collectionString'] or status['moreToCome']

    def _string_status(self, data
