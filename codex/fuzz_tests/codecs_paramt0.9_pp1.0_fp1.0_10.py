import codecs
codecs.register_error("skip", codecs.lookup_error("ignore"))

base="/agbs/schreibfehler_BergischGladbach.xlsx"
path=os.path.join(os.getcwd(), base)
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)
errors=[]
for row_index in range(sheet.nrows):
    high_value = sheet.cell_value(row_index, 0)
    #high_value = high_value.encode("utf-8")
    delimiter = ["",".",",","?","!",")","(","[","]","{","}","/","\\"]
    row_splitted = [high_value]
    for i in delimiter:
        new_value_list = []
        for value in row_splitted:
            new_values = value.split(i)
            for new_value in new_values:
                new_value_list.append(new_value)
        row_splitted = new_value_list
   
