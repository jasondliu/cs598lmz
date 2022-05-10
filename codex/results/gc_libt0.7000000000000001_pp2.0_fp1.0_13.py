import gc, weakref
from time import time

from logbook import Logger
from syscore.genutils import set_log_file
from syslogdiag.log import logtoscreen
from sysobjects.contracts import futuresContract
from syscore.genutils import str2Bool
from sysdata.futures.instruments import futuresInstrument
from sysdata.mongodb.mongo_connection import get_mongo_instrument_code
from sysdata.futures.instruments import futuresInstruments
from syslogdiag.log import logtoscreen

from sysdata.mongodb.mongo_connection import (
    MONGO_ID_KEY, mongoConnection, MONGO_PWD_KEY,
)

from sysdata.mongodb.mongo_connection import MONGO_FUTURES_DB_NAME

log = Logger("Mongo Futures Instruments")


class mongoFuturesInstrumentData(futuresInstruments):
    """

    Class to get instruments from a mongo database

    """

    def __init__(
       
