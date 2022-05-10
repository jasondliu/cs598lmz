import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from {}\n'.format(threading.current_thread().name))).start()

# 4. Создать функцию, которая создаст список из диапазона чисел введенных пользователем, удалит из него четные числа, а затем вернет результат.
# Вызвать функцию с аргументами 1 и 100.

def func7(begin: int, end: int):
    return [x for x in range(begin, end
