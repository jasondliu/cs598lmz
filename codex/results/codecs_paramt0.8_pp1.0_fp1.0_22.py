import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))
def process_text(text):
    text = unicode(text,'utf-8','replace_with_space')
    text = text.replace(u'\r', u'').replace(u'\n', u'')
    pattern = re.compile(u'[^\u0443\u0430\u0431\u0432\u0433\u0434\u0445\u0435\u0446\u0447\u0448\u0449\u044c\u044e\u044f\u0456\u0457\u0454\u0451\u0436\u0437\u0438\u0439\u043a\u043b\u043c\u043d\u043e\u043f\u044a\u044d\u0444\u0440\u0441\u0442\u0443\u0444\u0425\u0424\u0426\u0427\u0428\u
