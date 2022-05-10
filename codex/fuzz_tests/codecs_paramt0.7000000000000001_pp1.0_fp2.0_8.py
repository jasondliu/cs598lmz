import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

url = "www.baidu.com"
values = {'search': 'python'}
data = urlencode(values)
full_url = url + '?' + data
data = urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)
