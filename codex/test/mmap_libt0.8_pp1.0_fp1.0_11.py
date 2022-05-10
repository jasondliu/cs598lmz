import mmap
import json
import pprint
import os
from datetime import date
from dateutil.relativedelta import relativedelta
from typing import Any, Callable, Dict, List, Optional, Tuple

# TODO: Consider removing this to make the script more generic
import re
from string import Template

DEFAULT_MONTH = 1
DEFAULT_YEAR = 2017
DEFAULT_START_DATE_STR = '01/01/2017'
DEFAULT_END_DATE_STR = '12/31/2017'
TIME_DELTA_IN_MONTHS = 24

PROGRAM_NAME = 'budget_report'
LOGGER_NAME = 'budget_report'
DEFAULT_OUTPUT_FILE_NAME = 'budget_data_' + str(DEFAULT_MONTH) + '.' + \
    str(DEFAULT_YEAR) + '.csv'


