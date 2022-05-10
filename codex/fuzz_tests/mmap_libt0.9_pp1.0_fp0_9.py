import mmap
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openpyxl.utils.min_date import MIN_DATE

from utils.event_calculation import period_change, report_date_change
from core.excelworkbook import Workbook
from core.excelcell import Cell
from utils.events import Event, EventType, EventTable
from core.excelsheet import Worksheet
from core.box import Box, StyleBox


class Parameter:
    def __init__(self, id, name, event_type, value, date=None, date_reference=datetime.now()):
        self.id = id
        self.name = name
        self.event_type = event_type
        self.value = value
        self.date = date
        self.date_reference = date_reference
        if self.event_type == 1:
            self.event = Event(EventType(value), datetime.today())
        elif self.event_type == 2:
            if not self.date:
                self
