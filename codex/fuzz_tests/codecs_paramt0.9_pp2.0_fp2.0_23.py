import codecs
codecs.register_error('replace_with_space',replace_with_space)

#we remove all non-ascii characters to avoid getting UnicodeEncodeError while saving the result to csv file
def remove_non_ascii(text):
    return unidecode(text)

def correct_puncts(s):
#     if '&' in s:
#         s = s.replace('&', 'and')
#     if ',' in s:
#         s = ''.join(s).replace(',', ' ')
#     # if '"' in s:
#     #     s = ''.join(s).replace('"', '')
#     # if ';' in s:
#     #     s = ''.join(s).replace(';', ' ')
#     # if '!' in s:
#     #     s = ''.join(s).replace('!', '')
#     if '?' in s:
#         s = s.replace("?", " ")
#     if '(' in s:
#         s = s.replace("(", " "
