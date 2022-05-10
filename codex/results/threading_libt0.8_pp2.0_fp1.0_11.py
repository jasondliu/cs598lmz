import threading
threading.stack_size(102400)

global_start = time.time()

# constants
# ---------

# we are not using any of these
CAT_ALLOWED_IDS = [
    1,    # Компьютеры и комплектующие
    7,    # Игры, приставки и программы
    11,   # Книги и журналы
    13,   # Авто, мото
    15,   # Ремонт и строительство
    16,   # Дача, сад и огород
    17,   # Посуда и товары для кухни
    18,   #
