import ctypes
ctypes.windll.user32.MessageBoxW(0, "Ваши данные отправлены", "УСПЕШНО!", 0)


# In[ ]:


Код ниже создает форму в которой можно отправить комментарии от имени определенного пользователя.

from tkinter import *
import pandas as pd
import numpy as np
import time

#Создаем пустой pandas с сериями данных по пользователям
df = pd.
