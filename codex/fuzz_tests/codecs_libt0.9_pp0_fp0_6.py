import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def safe_html_security(value):
    # 安全编码
    soup = BeautifulSoup(value, "html.parser")
    return soup.prettify()


def set_all_value(key, value):
    try:
        result = cache.get(key)
        if result is None:
            cache.set(key, value)
        else:
            pass
    except Exception as e:
        print(e)


def get_all_value(key):
    try:
        result = cache.keys(key)
        # result = cache.get(key)
        if result is not None:
            return result
        else:
            return ""
    except Exception as e:
        print(e)


def del_all_value(key):
    try:
        result = cache.delete(key)
        if result is not None:
            return result
        else:
            return ""

