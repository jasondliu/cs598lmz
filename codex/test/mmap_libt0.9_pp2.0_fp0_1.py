import mmap
import os
import sys

class TOC(object):
    """
    Represents an SQLite table of contents
    """

    class Page(object):
        """
        Represents an SQLite page
        """

        def __init__(self, table, offset):
            """
            Structure of a page...
            0x0000-0x0003: Page number
            0x0004-0x0005: Number of cells on this page
            0x0006-0x0007: First cell offset
            0x0008-0x0009: Header data size
            0x000A-0x000B: Right sibling number
            0x00?{-0x00?}: Types of cells on this page.
            0x????-0x????: Page offset for the cells
            0x00?{-0x00?}: Data dependent on the cell
            0x00?{-0x00?}: Free data
            """
            self.__table = table
            self.__offset = offset
            self.__bytes = table.map[offset:offset+16]

