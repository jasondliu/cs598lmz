import bz2
bz2.BZ2File(f).read()

# теперь все равно не получается
# пробовал параметры:
# encoding='utf-8'
# errors='ignore'
# и их комбинации
</code>
Содержимое файла:
<code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE yml_catalog SYSTEM "shops.dtd"&gt;
&lt;yml_catalog date="2016-07-26 12:00"&gt;
&lt;shop&gt;
&lt;name&gt;Сумки, рюкзаки и кошельки&lt;/name&gt;

