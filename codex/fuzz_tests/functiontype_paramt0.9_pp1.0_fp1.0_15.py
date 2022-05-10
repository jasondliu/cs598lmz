from types import FunctionType
list(FunctionType(m_test.co_consts[2], {})())


print(list(map(lambda x: x[3:-3], re.findall('<a class="blog_title" href="(.*?)">(.*?)</a>', urllib.request.urlopen('http://blog.sina.com.cn/u/1861413813').read().decode('utf-8')))))

print(list(filter(lambda x: x > 20, range(10, 52, 5))))

m_test = lambda x: ''.join(list(map(lambda x: str(x % 2) + ' ' + x, filter(lambda x: x > 20, range(10, 52, x)))))
print(m_test(5))


print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])))
#--------------------------------------------------------------------------------------------------#


#------------------------------某些while循环的改写------------------------------------------------#
s = 'cdefghijkdefpr'  # 找
