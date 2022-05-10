import bz2
bz2.compress()

import csv

# line.decode('utf-8')

def ask_exit(action, text):
    try:
        if input('\n' + text).lower() in ['верно', 'верный']:
            return True
        elif input('\n' + action).lower() in ['да', 'д']:
            return False
    except:
        return False

def modify():
    file = input('Введите полное название файла\n>>> ')
    remove = input('Если вы хотите удалить строки из документа введите 1\n' +
                  'Если вы хотите заменить строки
