import io
class File(io.RawIOBase):
    """
    Class File is a RawIOBase to represent and deal with the data of the file.
    The file can be empty, so it is created with a number of bytes and a name.
    It is possible to write and read from file
    """
    def __init__(self,name,number=0):
        self.__name=name
        self.__number=number
        self.__file=io.BytesIO()

    def __str__(self):
        """
        toString method to return the name and the number of bytes

        Returns
        -------
        str
            The name of the file and the number of bytes
        """
        return str(self.__name)+" - "+str(self.__number)+" bytes"

    def __del__(self):
        """
        Destructor
        """
        self.__file.close()

    @property
    def number(self):
        """
        Method to get the number of bytes

        Returns
        -------
        int
            The number of bytes
        """
        return self.__number

    @property

