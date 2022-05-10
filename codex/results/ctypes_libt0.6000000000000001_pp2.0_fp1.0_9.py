import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# -*- coding: utf-8 -*-

import ctypes
ctypes.windll.user32.MessageBoxW(0, u"Your text", u"Your title", 1)

# -*- coding: utf-8 -*-

import ctypes
ctypes.windll.user32.MessageBoxW(0, u"Ваш текст", u"Ваш заголовок", 1)
</code>
Скриншот:

В документации написано:
<blockquote>
<p>The maximum length, in characters, of the text in the edit control. If
  the text exceeds this limit, the user cannot type or paste additional
  text.</p>
</blockquote>
Так вот надо ли
