import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_data_from_csv(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def write_data_to_csv(data, file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

def get_data_from_excel(file_name):
    data = []
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active
    for row in ws.rows:
        row_data = []
        for cell in row:
            row_data.append(cell.value)
       
