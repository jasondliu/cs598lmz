import weakref
from collections import defaultdict

import numpy as np

from pynwb.ecephys import ElectricalSeries

from . import util


class RecordingGroup:
    """A group of recordings, with one cache for each recording."""

    def __init__(self, parent, cache=None):
        self.parent = weakref.ref(parent)
        self.recordings = []
        self._lookup_dict = None

        self.cache = cache

    def add_recording(self, rec):
        assert isinstance(rec, Recording)
        self.recordings.append(rec.name)

        if self.cache is not None:
            assert rec.cache is None
            rec.cache = RecordingCache(parent=self, name=rec.name)

    @property
    def lookup_dict(self):
        if self._lookup_dict is None:
            self._lookup_dict = {
                rec: getattr(self.parent(), '{}_{}'.format(self.parent().name, rec))
                for rec in self.recordings
            }
       
