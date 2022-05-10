import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
from dateutil.parser import *
from web.controllers.main import CSVStorage
from itertools import product
import re


class hr_overtime(models.Model):
    _name = 'hr.overtime'
    _rec_name = 'employee_id'
    _order = 'date_start'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date_start = fields.Datetime(string='Start Date', required=True)
    date_end = fields.Datetime(string='End Date', required=True)
    reason = fields.Text(string='Reason')
    overtime_type = fields.Selection([
        ('Hari Normal', 'Hari Normal'),
        ('Hari Libur', 'Hari Libur'),
        ('Hari Besar',
