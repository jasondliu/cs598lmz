import ctypes
ctypes.windll.user32.ShowWindow(h, 0)

# set window size
import os
os.system('mode con: cols=100 lines=150')
import pyautogui as pg
pg.press('tab')

# Set Coordinates
pg.click(40, 100)
pg.click(40, 100)
pg.click(40, 100)

pg.hotkey('ctrl','a')
execute('ctrl','c','1')
pg.hotkey('alt','l','alt','o','','','','','','','','','','','','','','','tab','tab')
execute('ctrl','v')
pg.hotkey('alt','a','f')

pg.hotkey('alt','l','alt','o',pg.press('down'),pg.press('down'),'','','',pg.press('down'),'','','','pg.press('down'),'''pg.press('down'),'pg.press('down),'pg.press('down),''pg.press('down),'pg.press('down),pg.press('down)
execute('ctrl','a')
execute
