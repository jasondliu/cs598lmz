from types import FunctionType
list(FunctionType(lambda x: x**2, globals(), 'f'))

# 4. Напишите декоратор non_empty, который дополнительно проверяет списковый результат
# любой функции: если в нем содержатся пустые значения (пустые строки, None, пустые списки),
# то они удаляются.
# Примеры использования:
# @non_empty
# def get_pages
