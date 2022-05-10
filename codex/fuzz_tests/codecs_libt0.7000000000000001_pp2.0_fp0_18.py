import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import xlrd
import csv
from sys import argv

#打开excel文档
def read_excel(filename):
    excel_table = xlrd.open_workbook(filename)
    sheet_name = excel_table.sheet_names()[0]
    sheet_obj = excel_table.sheet_by_name(sheet_name)
    return sheet_obj

#输出到csv文件
def write_csv(csv_name,data):
    with open(csv_name,'w',encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in data:
            csv_writer.writerow(row)

#读取excel每一列的数据，生成一个数据列表
def excel_to_csv(
