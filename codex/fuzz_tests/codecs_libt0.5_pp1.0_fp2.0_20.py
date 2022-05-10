import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Create a file to write to, add headers row
with open('c:\\users\\james\\desktop\\parsed.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(['Date', 'Description', 'Amount'])

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('c:\\users\\james\\desktop\\test.xlsx')
sh = wb.sheet_by_index(0)

# List to hold dictionaries
parsed = []

# Iterate through each row in worksheet and fetch values into dict
for row in range(1, sh.nrows):
    d = {}
    d['Date'] = sh.cell_value(rowx=row, colx=0)
    d['Description'] = sh.cell_value(rowx=row, colx=1)
    d['Amount'] = sh.cell_value
