import mmap, os
from xlrd import open_workbook, xldate_as_tuple
from xlutils.copy import copy
from datetime import date
import math
from Common import Common


# 初始化xls表
class Init_xls(Common):
    def __init__(self, fileName):
        self.filename = fileName
        self.workbook = open_workbook(self.filename)
        self.init_worksheet()

    def init_worksheet(self):
        # 工作页的个数，也是工作页的索引从0开始
        self.WorksheetNum = len(self.workbook.sheets())
        self.worksheet_name = []
        for i in range(self.WorksheetNum):
            self.worksheet_name.append(self.workbook.sheet_by_index(i).name)
            self.SheetNum = i

    def on_read_worksheet(self, sheet_index):
       
