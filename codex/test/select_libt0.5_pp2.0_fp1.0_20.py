import select
import logging
import threading
import os
import time
import sys
import traceback

#-------------------------------------------------------------------------------

class Pipe():
    """
    A pipe is used to communicate between two threads.
    """
    
    def __init__(self, name=None):
        # Create the pipe.
        self.__read_fd, self.__write_fd = os.pipe()
        
        # Set the name of this pipe.
        self.__name = name
        
        # Set the initial state of the pipe.
        self.__is_open = True
        self.__is_closed = False
        
    def __del__(self):
        # Close the pipe.
        self.close()
        
    def __str__(self):
        return "Pipe(name=%s)" % self.__name
        
    def fileno(self):
        """
        This function returns the file descriptor for this pipe.
        """
        return self.__read_fd
        
    def close(self):
        """
        This function closes the pipe.
        """
