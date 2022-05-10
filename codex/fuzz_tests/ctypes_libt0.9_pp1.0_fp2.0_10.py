import ctypes
ctypes.windll.user32.SystemParametersInfoW(20,0,u"C:\\Users\\USER\\Desktop\\Python\\Captcha\\Captcha\\123.jpg",0)
</code>
Обновление:
Проблема решилась. Путь к картинке был неправильным. Поменял на абсолютный, всё стало ок. Благодарю всех.


A:

Правильно писать так:
<code>path = u'C:\\Users\\USER\\Desktop\\Python\\Captcha\\Captcha\\123.jpg'
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

