import gc, weakref
from schlichtanders.mycontextmanagers import ignored
from itertools import count
import logging
import numpy as np

__all__ = ["TrackRecord", "Player", "player", "TrackRecordPlayer"]

logger = logging.getLogger(__name__)

from .utils import discard_all, compact_objs, compact, gc_compact


class TrackRecord(object):
    """
    Record track and mainly used for logging

    Implements: ``__getattr__``, ``__setattr__``
    """
    def __init__(self, name, player, record=None):
        """
        :param name: name of the track
        :param player: player to record the track
        :param record: record to copy from
        """
        # init with self name and player
        self.__name = name
        self.__player = player
        # set default record
        self.__track = {}

        # if we want to copy values from another record
        if record is not None:
            track = record.track
            for cmd, args
