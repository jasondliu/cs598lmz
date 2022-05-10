import weakref

class HashableSet(collections.abc.Set):
    def __new__(cls):
        new_instance = super().__new__(cls)
        # Using a weak key dictionary, to make sure that key is discarded whenever it is no longer
        #  referenced in the program. It does not have any references in the instance variables,
        # hence it gets garbage collected.
        new_instance._dictionary = weakref.WeakKeyDictionary()
        return new_instance

    def __hash__(self):
        return hash(id(self))

    def __contains__(self, key):
        return hash(key) in self._dictionary

    def add(self, key):
        # Saving the key as a weak reference, to make sure key is collected when it is no longer
        # referenced in the program
        self._dictionary[key] = None

def main():
    s = HashableSet()
    s.add(1)
    s.add(2)
    s.add("The")
    
    # Testing if 3 is present in the set
   
