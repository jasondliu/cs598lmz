import mmap

__author__ = 'Justin Jansen'
__status__ = 'Development'
__date__ = '03/23/14'


class ReadFile(object):
    """
    A class to read a file and return results.
    """
    def __init__(self, file_to_read):
        """
        Initializes the ReadFile object.
        :param file_to_read:
        :return:
        """
        self.file_to_read = file_to_read

    def read_file_line_by_line(self):
        """
        Reads the file line by line and stores each line as an element in a list.
        :return:
        """
        with open(self.file_to_read) as file_handle:
            file_contents = file_handle.readlines()
        return file_contents

    def read_file_mmap(self):
        """
        Reads the file using the mmap file module
        and stores each line as an element in a list.
        :return:
        """
