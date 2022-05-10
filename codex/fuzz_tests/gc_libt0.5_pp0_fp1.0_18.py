import gc, weakref
import xlrd
import xlwt
from xlutils.copy import copy
import xlwt
import os

class Excel_Data():
    def __init__(self,filepath,sheetname):
        self.filepath=filepath
        self.sheetname=sheetname
        self.data=xlrd.open_workbook(self.filepath)
        self.table=self.data.sheet_by_name(self.sheetname)
        self.keys=self.table.row_values(0)
        self.rowNum=self.table.nrows
        self.colNum=self.table.ncols
        self.curRowNo=1
    def next(self):
        r=[]
        while self.hasNext():
            s={}
            col=self.table.row_values(self.curRowNo)
            i=self.colNum
            for x in range(i):
                s[self.keys[x]]=col[x]
            r.append(s)
            self.curRowNo+=1
        return
