import threading
threading.Thread(target=lambda: submitFile('file/' + img_paths2)).start()
# threading.Thread(target=lambda: submitFile('file/' + img_paths3)).start()
# threading.Thread(target=lambda: submitFile('file/' + img_paths4)).start()
# threading.Thread(target=lambda: submitFile('file/' + img_paths5)).start()

threading.Thread(target=lambda: submitFile('file/' + img_paths1)).start()
threading.Thread(target=lambda: submitFile('file/' + img_paths0)).start()
threading.Thread(target=lambda: submitFile('file/' + img_paths6)).start()
threading.Thread(target=lambda: submitFile('file/' + img_paths7)).start()
threading.Thread(target=lambda: submitFile('file/' + img_paths8)).start()
threading.Thread(target=lambda: submitFile('file/' + img_paths9)).start()

