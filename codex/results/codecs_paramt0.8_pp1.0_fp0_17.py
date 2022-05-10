import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)
import os
import sys
import re
import json
import glob

from lex.oed.thesaurus.matchkeys import MatchKey


class EntryList(object):

    """

    Data container for a list of thesaurus entries.
    """

    def __init__(self):
        self.entries = {}
        self.matchkeys = MatchKey()
        self.ids = {}

    def add_entries(self, entries):
        """

        :param entries:
        :return:
        """
        for entry in entries:
            self.add_entry(entry)

    def add_entry(self, entry):
        """

        Add an entry to the list.
        This also updates the matching key index.

        :param entry:
        :return:
        """
        key = self.matchkeys.make_key(entry)
        if key is not None:
            if key in self.entries:
                self.entries[key].append(entry)
            else:
                self.ent
