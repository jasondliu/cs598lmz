import codecs
codecs.register_error('Strict', codecs.ignore_errors)

import xlsxwriter

from openpyxl.styles import Font, Color
from openpyxl.styles import colors
from openpyxl.cell import get_column_letter
from openpyxl import Workbook
from openpyxl.utils import get_column_interval, coordinate_from_string
from openpyxl.worksheet.datavalidation import DataValidation

from gooey.gui.util.quoting import quote


#todo: option to automatically generate a file name
class ExportCommand(object):
    def __init__(self, data, file_format):
        self.data = data
        self.file_format = file_format
        self.filename = None
        self.output = []
        self.rows = []

    def generate(self):
        for arg in self.data:
            self.rows.append([arg.name, arg.value])

        if self.file_format == 'csv':
            self.generate_csv()
        elif self.file_format == 'ex
