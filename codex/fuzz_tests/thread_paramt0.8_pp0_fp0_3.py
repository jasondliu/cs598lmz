import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n' * 5)).start()

def get_numbers(num):
    num = int(num)
    print("get_numbers")
    for i in range(num):
        print(i)


# Исходные данные
print("Введите количество строк для подсчета: ")
num = input()
# Создадим поток для вычисления чисел
t = threading.Thread(target=get_numbers, args=[num])
# Запускаем поток
t.start()

print("Посчитали!")

# завершить поток
t.join()
