import sys, threading
threading.Thread(target=lambda: sys.stderr.write('Hello stderr!\n')).start()
print('Hello stdout')

# Type Conversion
x = 5
x = float(5)
print(x)
x = 5.6
x = int(5.6)
print(x)
x = 2
print(complex(x))
print(complex(x,1))
x = 5.6
x = round(x)
print(x)

s = 'Hello World'
x = str(s)
print(x)
s = '5'
x = int(s)
print(x)
s = '5.6'
x = float(s)
print(x)
s = '5 + 2j'
x = complex(s)
print(x)

# Binary Conversion
x = 5
print(bin(x))
x = 0b101
print(x)
x = int('101',2)
print(x)
x = 0o71
print(x)
x = int('71',8)
print(x)
