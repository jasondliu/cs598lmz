import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# короткий вариант с помощью функции eval
# eval(input())

# короткий вариант с помощью функции compile
# compile(input(), '', 'single')

# короткий вариант с помощью функции exec
# exec(input())

# короткий вариант с помощью функции compile
# exec(compile(input(), '', 'single'))

# короткий вариант с помо
