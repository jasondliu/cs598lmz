import codecs
codecs.open("hello.txt", "w", "utf-8")

# Застрахуемся на случай Python 2.7, когда у нас нет модуля codecs
# Надо добавить код, чтобы он проверял наличие codecs, и делал всё, что
# нам надо, если codecs недоступна. Но это будет не тривиально, 
# потому что если мы сейчас пишем код, его
