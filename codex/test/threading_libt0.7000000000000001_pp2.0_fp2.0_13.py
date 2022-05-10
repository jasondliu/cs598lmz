import threading
threading.Thread(target=lambda:
  subprocess.call(["python", "manage.py", "runserver", "8000"])).start()
subprocess.call(["python", "bot.py"])
