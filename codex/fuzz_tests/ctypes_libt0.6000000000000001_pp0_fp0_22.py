import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
В данном случае последний параметр указывает на наличие кнопки ОК. Есть ли где-нибудь информация про остальные параметры?


A:

Попробуйте так:
<code>import ctypes

ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
Параметры:

первый параметр - деск
