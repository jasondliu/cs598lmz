import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import logging
# logging.basicConfig(
#     level = logging.DEBUG,
#     format = '%(asctime)s %(levelname)s %(message)s',
#     filename = 'log.txt',
#     filemode = 'w'
# )

# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

# print('Hello world!')

# name = input('Please input your name: ')
# print('Hello, ', name)

# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)

# print('I\'m \"OK\"!')
# print(r'\\\t\\')
# print('''line1
# line2
# line3''')

# print(True and True)
# print(True or False)
# print(
