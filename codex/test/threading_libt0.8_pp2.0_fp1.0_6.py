import threading
threading.stack_size(2**27)
import multiprocessing


class Parser:
    def __init__(self, input_path):
        self.input = input_path
        self.output = "./data/gimli_input.txt"
        self.int_table, self.obj_table, self.relationships = Parser.parse_input(self.input)
        self.int_table_size = len(self.int_table)
        self.obj_table_size = len(self.obj_table)
        self.relationship_size = len(self.relationships)

    # Get the integer representation for an object
    # obj: the object in question
    # obj_table: the table translating objects to integers
    #
    # return: obj's integer representation
    def get_obj_int(self, obj):
        if obj not in self.obj_table:
            self.obj_table_size += 1
            self.obj_table[obj] = self.obj_table_size

        return self.obj_table[obj]

    #
