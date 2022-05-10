import socket
import re
import time

# Максимальный размер пакета для передачи
TCP_PACKET_MAX_SIZE = 4096
# Соответствующие коды сообщений сервера
PRESENCE_CODE = 100
RESPONSE_CODE = 200
ERROR_CODE = 400
# Формат приветствия сервера
PRESENCE_MESSAGE = '{} {} {}\n{}'
# Формат ответа сервера
RESPONSE_MESSAGE = '{} {} {}'


# Функция инициализации к
