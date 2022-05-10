import threading
threading.Thread(target=lambda : os.system('echo "linus rocks!"')).start()
# or 
threading.Thread(target=lambda : print('linus rocks!')).start()
```
