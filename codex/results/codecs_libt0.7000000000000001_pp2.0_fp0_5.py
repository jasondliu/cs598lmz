import codecs
codecs.open('', 'r', encoding='utf-8')
 
def generate_tf_idf(text, names):
    # пустой список для заполнения
    tf_idf = []
    # перебираем входящее местоимение и преобразуем его в нижний регистр
    for name in names:
        # переводим в нижний регистр
        name = name.lower()
        # если местоимение входит в текст
        if name in text:
            # вычисляем т
