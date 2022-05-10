import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000))))).start()

# Пример использования:
# python3 -m timeit -n 1000 -s "import test" "test.foo()"
# 1000 loops, best of 5: 0.5 usec per loop

# python3 -m timeit -n 1000 -s "import test" "test.foo()"
# 1000 loops, best of 5: 0.9 usec per loop

# Почему быстрее на маленьких объёмах данных?
# Потому что на маленьких объёмах данных время выполнения кода
