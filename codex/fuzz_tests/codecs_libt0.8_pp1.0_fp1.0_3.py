import codecs
codecs.open('C:\\Users\\User\\Downloads\\all.txt', 'r', 'utf-16').read()
</code>
Получаю ошибку
<code>**File "C:\Users\User\Desktop\python.py", line 1
SyntaxError: encoding problem: utf-16**
</code>
Как правильно открыть файл используя кодировку utf-16?


A:

Для выполнения команды <code>codecs.open()</code> необходимо предварительно импортировать модуль <code>codecs</code> командой
