import ctypes
import ctypes.util
import threading
import sqlite3
import time

# Поставить курсор в любую функцию класса MyClass и нажать F2 (Modules-View
# Hierarchy)
# Чтобы просмотреть функцию кликните на имени функции и нажмите ENTER
class MyClass():
    def func1():
        pass

    def func2():
        pass


spam = MyClass

print(spam.__name__)  # MyClass

print()

# Причина – в дружественных отношениях между файл
