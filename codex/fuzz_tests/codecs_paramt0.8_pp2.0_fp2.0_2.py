import codecs
codecs.register_error('decode_russian', codecs.decode)

# Открываем файл результатов
result_file = open('result.txt', 'w', encoding='utf-8')


# Добавляем статьи из Интернета
def add_articles():
    length = len(links)
    i = 0

    # Проходим по ссылкам
    for link in links:
        # Получаем страницу
        page = requests.get(link)
        page = page.text

        # Создаем объект типа BeautifulSoup и передаем ему html-код страницы
        soup = BeautifulSoup
