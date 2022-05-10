import weakref
import functools

from model import Model
from exceptions import *

class Table(object):
    """
    Represents the tables in the database.  Stores the columns and constraints.
    """

    _table_name = None
    _columns = None
    _constraints = None

    def __init__(self, name, columns, constraints=None):
        """
        Create a new table.
        @param name: name of the table
        @param columns: list of columns
        @param constraints: constraints on the table (optional)
        """
        self._table_name = name
        self._columns = columns
        self._constraints = constraints
        self.create_class()

    @property
    def table_name(self):
        """
        Get the name of the table.
        @return: name of the table
        """
        return self._table_name

    @property
    def columns(self):
        """
        Get a list of columns in the table.
        @return: list of columns
        """
        return self._columns

   
