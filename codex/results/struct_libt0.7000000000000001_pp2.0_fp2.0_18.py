import _struct
from _struct import *


class Protocol:
    """
    протокол коммуникации по протоколу TCP/IP
    представляет собой обертку над классом сокетов
    все данные передаются в виде байтового строки
    """
    # структура заголовка протокола
    _struct_header = Struct(
        '<'  # порядок байтов LITTLE_ENDIAN
        'H'  # длина поля FROM
        'H' 
