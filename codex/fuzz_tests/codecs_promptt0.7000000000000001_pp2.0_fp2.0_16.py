import codecs
# Test codecs.register_error()
# with codecs.open('text.txt', encoding='utf-8') as f:
#     try:
#         while True:
#             line = next(f) # get next line
#     except StopIteration:
#         pass
#     except UnicodeDecodeError as e:
#         print(e)
#         # replace undecodeable bytes
#         print(e.object[e.start:e.end])
#         line = line[:e.start] + b'?' * (e.end - e.start) + line[e.end:]
#     print(line)
# from codecs import register_error
# def handle_error(err):
#     return ('?', err.start + 1)
# register_error('handle', handle_error)
# with codecs.open('text.txt', encoding='utf-8', errors='handle') as f:
#     for line in f:
#         print(line.strip())
# from codecs import lookup
# print(lookup('utf-8').name)
# print(lookup('
