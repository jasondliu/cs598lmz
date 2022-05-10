import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threaded')).start()

# Generator expression
print('Generator expression')

print(sum(i * i for i in range(10)))  # sum of squares

# Dictionary comprehension
print('Dictionary comprehension')

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food'])  # Fetch value of key 'food'
D['quantity'] += 1  # Add 1 to 'quantity' value
print(D)

# Nested code structures
print('Nested code structures')

if 'f' in 'food':
    print('f in food')
    if 'o' in 'food':
        print('o in food')
        if 'o' in 'food':
            print('o in food')
            if 'd' in 'food':
                print('d in food')

print('-' * 40)

# Nested code structures with elif
print('Nested code structures with elif')

x = 'killer rabbit'

