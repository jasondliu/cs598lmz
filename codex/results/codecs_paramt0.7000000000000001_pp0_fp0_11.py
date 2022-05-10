import codecs
codecs.register_error('replace_spaces', lambda e: (u' ',e.start + 1))

# for node in soup.find_all('tr', id=re.compile('^t')):
#     try:
#         text = node.get_text()
#         text = text.encode('utf-8')
#         print text
#     except UnicodeEncodeError:
#         print text

# with open('output.txt', 'w+') as f:
#     f.write(str(soup.find_all('tr')))


# data = soup.find_all('td')
#
# for d in data:
#     print d.get_text()
