import codecs
# Test codecs.register_error('strict', strict_errors)
def get_normalized_trans(text):
    try:
        text_transformed = text.translate({0x201D:0x22, 0x201C: 0x22, 0x2018:0x27, 0x2019:0x27})
        return text_transformed
    except:
        return text
# Get data from source files

def get_source_data():
    fail = False
    if fail:
        with open(source_file_path, 'rb') as f:
            data = [get_normalized_trans(x.decode('utf8')) for x in f.readlines()]
    else:
        try:
            with open(source_file_path, 'rb') as f:
                data = [get_normalized_trans(x.decode('utf8')) for x in f.readlines()]
        except UnicodeDecodeError:
            with open(source_file_path, 'rb') as f:
                data = [get_normalized_trans(x.decode('l
