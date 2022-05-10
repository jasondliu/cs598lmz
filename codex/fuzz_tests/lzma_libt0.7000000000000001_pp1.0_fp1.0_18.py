import lzma
lzma.open('...')
</code>
Выдаёт такую ошибку:
<code>Traceback (most recent call last):
  File "&lt;pyshell#0&gt;", line 1, in &lt;module&gt;
    lzma.open('E:/Документы/Загрузки/enwiki-20180901-pages-articles-multistream.xml.bz2')
  File "C:\Users\Леонид\AppData\Local\Programs\Python\Python36\lib\lzma.py", line 65, in open
    with _FileInContext(filename, mode, **kwargs) as f:
  File "C:\Users\Леонид\AppData\Local\Programs\Python\Python36\lib\contextlib.py", line 81, in __enter__
    return next(self.gen)
  File "C:\Users\Леони
