import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Загружаем все файлы по папкам
def load_files(path):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.append(os.path.join(root, filename))
    return files

# Преобразование данных в массив
def load_data(files):
    data = []
    for file in files:
        with codecs.open(file, 'r', 'utf-8', 'ignore') as f:
            text = f.read()
            data.append(text.lower())
    return data

# Создание словаря и матрицы
