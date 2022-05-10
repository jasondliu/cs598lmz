import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from secondary thread!\n')).start()
sys.stdout.write('Hello from main thread!\n')
x = 0
x = x + 1
x
x
x + 1
x
x + 2
def add1(z):
    return z + 1
add1(2)
add1(add1(2))
 
add1(1)
add1(2)
add1(add1(2))
add1(add1(3))
add1(add1(add1(3)))
add1(add1(add1(add1(3))))
add1(add1(add1(add1(add1(3)))))
add1(add1(add1(add1(add1(add1(3))))))
add1(add1(add1(add1(add1(add1(add1(3)))))))
add1(add1(add1(add1(add1(add1(add1(add1(3))))))))
add1(add1(add1(add1(add1(
