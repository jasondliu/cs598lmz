import codecs
codecs.register(lambda x: codecs.lookup('utf-8') if x == 'cp65001' else None)


def to_unicode(text):
    if isinstance(text, str):
        try:
            text = text.decode('utf-8')
        except UnicodeError:
            text = text.decode('cp1251')
    return text


def to_utf8(text):
    if isinstance(text, unicode):
        text = text.encode('utf-8')
    return text


def decode_dict_values(d, recursive=False, dict_only=False, list_only=False):
    """
    Декодирование значений словаря из байтов в строки.
    Также декодирует все словари в списка
