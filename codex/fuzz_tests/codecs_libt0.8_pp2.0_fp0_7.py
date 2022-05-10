import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def save_data_to_csv(data, file_name, file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    #file_path_name=os.path.join(file_path, file_name) + '.xlsx'
    file_path_name=os.path.join(file_path, file_name) + '.csv'
    if len(data)==0:
        print('data is null!')
    else:
        try:
            #data_frame = pd.DataFrame(data, columns=['date', 'stock_num', 'name', 'funds_num', 'stock_ratio'])
            #data_frame.to_excel(file_path_name, index=False)
            #my_sheet = 'Sheet1'
            #book = load_workbook(file_path_name)
            #writer = pd
