import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Программа проверки работы принтера")

import win32print
import win32ui
from win32 import win32gui
import os
import time

def print_file(file_name):
    # Получаем имя принтера по умолчанию
    printer_name = win32print.GetDefaultPrinter ()
    # Получаем дескриптор принтера
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    # Настраиваем принтер
    hDC.SetMapMode (win32con.MM_TWIPS)
    # Создаем о
