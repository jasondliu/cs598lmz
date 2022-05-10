import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# пример с получением значения из диалогового окна
# import ctypes
# user32 = ctypes.windll.user32
# user32.MessageBoxW(None, u"Привет мир!", u"Пример сообщения", 0)
# Пример использования диалогового окна с кнопками "Да" и "Нет"
# import ctypes
# user32 = ctypes.windll.user32
# if user32.MessageBoxW(None, u"Вы действите
