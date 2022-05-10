import select

import lib.report_to_csv as report_to_csv

sys.path.append('../')
from lib.log_and_statistic import log_and_statistic
from lib.check_login import check_login
from lib.connect import connect
from dict_key_value import dict_key_value


@log_and_statistic
def report_running_version(func):
    def wrapper(self, *args, **kwargs):
        result_report = func(self, *args, **kwargs)
        self.result_report['running_version'] = result_report
    return wrapper


@log_and_statistic
def report_running_version_of_slb(func):
    def wrapper(self, *args, **kwargs):
        result_report = func(self, *args, **kwargs)
        self.result_report['running_version_slb'] = result_report
    return wrapper


class SlbReport():
    def __init__(self):
        self.result_report = {}
        self.result_report['
