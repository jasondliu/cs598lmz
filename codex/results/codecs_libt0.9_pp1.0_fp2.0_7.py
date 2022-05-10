import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)


csv_file =open('fog_data.csv')
csv_data =csv.reader(csv_file)

def data_early_stages(original_data):
    early = []
    for i in range(0, 705):
        early.append(original_data[i])
    
    return early
early = data_early_stages(list(csv_data))

def data_late_stages(original_data):
    late = []
    for i in range(706, 1412):
        late.append(original_data[i])
    
    return late
late = data_late_stages(list(csv_data))


def convert_time_to_datatime(dataset):

    for i in dataset:
        i[0] = pd.to_datetime(i[0])

    return dataset

csv_time_data = convert_time_to_datatime(early)

def
