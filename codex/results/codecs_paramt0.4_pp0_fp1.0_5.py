import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

# чтение из файла
def read_file(file_name):
    f = codecs.open(file_name, 'r', 'utf-8', errors='replace_with_space')
    text = f.read()
    f.close()
    return text

# запись в файл
def write_file(file_name, text):
    f = codecs.open(file_name, 'w', 'utf-8')
    f.write(text)
    f.close()

# перевод в нижний регистр
def to_lowercase(text):
    return text.lower()

# удаление знаков препинания
def remove_punctuation(text):

