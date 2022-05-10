import types
types.StringType = types.UnicodeType

import win32com.client
import pythoncom

pythoncom.CoInitialize()

import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    stream=sys.stdout)

import win32com.client

class Word:
    """
    Класс для управление приложением MS Word
    """
    def __init__(self, visible=False):
        """
        Конструктор
        """
        # Запускаем MS Word
        self._winWord = win32com.client.Dispatch("Word.Application")
        # Устанавливаем видимость.
        self._winWord.Visible = visible

    def __del__(self):

