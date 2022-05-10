import ctypes
ctypes.windll.user32.MessageBoxW(0, u"Error message!", u"Error", 0 )
</code>
Проблема в том, что эта функция показывает диалоговое окно над всеми остальными окнами и не позволяет сворачивать основное окно. Как быть?


A:

Если используется PyQt:
<code>from PyQt5 import QtWidgets
QtWidgets.QMessageBox().critical(None, "Error", "Error message!")
</code>

