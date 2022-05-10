import mmap
import numpy as np
import tqdm

class Day(object):
    def __init__(self, year, month, day, usage):
        self.year, self.month, self.day = year, month, day
        self.usage = usage

    @classmethod
    def from_string(cls, line):
        year, month, day = map(int, line[:8].split('/'))
        tokens = line[8:].split()
        usage = float(tokens[1])
        return cls(year, month, day, usage)


class Month(object):
    def __init__(self, year, month, usage):
        self.year, self.month = year, month
        self.usage = usage


class Utility(object):
    """An object to represent a single utility company and bill to callers."""
    def __init__(self, filename, granularity='day'):
        self.filename, self.granularity = filename, granularity
        self.usage = self.load_usage()

    def load_usage(
