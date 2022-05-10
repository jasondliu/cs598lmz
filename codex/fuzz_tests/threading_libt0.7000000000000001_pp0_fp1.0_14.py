import threading
threading.Thread(target=threading.Thread(target=print, args=('Cats',))).start()

# решение автора

import threading

threading.Thread(target=print, args=('Cats',)).start()

# первый поток (target=print) не требует аргументов, а второй поток (args=('Cats',)) требует аргумент)

# если написать как в предыдущем решении, то в качестве target указывается threading.Thread, которая требует
