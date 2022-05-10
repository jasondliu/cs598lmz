import codecs
# Test codecs.register_error
with codecs.open('somefile.abc', 'w', encoding='abc') as f:  #absent encoding
    # mycodec.register_error('test', lambda e: ('',e.end))
    f.write('some text')


"""
Пример приведённый выше обнаруживается стандартным процессором
(при сборке в пакет ядра фреймворка) и предоставляет неопределённое поведение
(может пройти без исключения или гене
