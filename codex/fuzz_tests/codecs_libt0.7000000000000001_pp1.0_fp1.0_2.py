import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Open a workbook
def open_xls_as_xlsx(filename):
    # first open using xlrd
    xls_workbook = xlrd.open_workbook(filename)
    # now convert to xlwt
    xlsx_workbook = Workbook()
    # add all the sheets from the xls file
    for xls_sheet in xls_workbook.sheets():
        xlsx_workbook.add_sheet(xls_sheet.name)
        # copy over the cells
        for row in range(xls_sheet.nrows):
            for col in range(xls_sheet.ncols):
                xlsx_workbook.get_sheet(xls_sheet.name).write(row, col, xls_sheet.cell_value(row, col))
    # save
    return xlsx_workbook

# Open a workbook
workbook = xlrd.open_workbook('
