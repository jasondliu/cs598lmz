import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input()), daemon=True).start()

# Пример вызова
# python3 async_input.py
# Ввод:
# abc
# Вывод:
# abc
