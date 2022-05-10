import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)


# Массив для хранения данных о директориях
dirs_list = []


# Функция поиска файлов по заданной маске
def search_files(path, mask):
    # Перебираем переданный путь по файлам
    for entry in os.listdir(path):
        # Создаем полный путь к файлу
        full_path = os.path.join(path, entry)
        # Если пут
