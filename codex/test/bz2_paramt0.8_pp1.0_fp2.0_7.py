from bz2 import BZ2Decompressor
BZ2Decompressor()

class PersonManager:
    def __init__(self, path):
        # The path to where our pickled data is stored
        self.__data_file = os.path.join(path, "people.bin")
        # The actual data buffer; a dictionary mapping names to the associated Person objects
        self.__data = {}

        if os.path.exists(self.__data_file):
            self.__load()

    def add(self, person):
        self.__data[person.name] = person

    def remove(self, name):
        del self.__data[name]

    def get(self, name):
        return self.__data[name]

    def count(self):
        return len(self.__data)

    def names(self):
        return self.__data.keys()

    def items(self):
        return self.__data.items()

