import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
db = sqlite3.connect(":memory:")
db.cursor().execute("select * from sqlite_master")

# Test ctypes.util.find_library("sqlite3")
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# Test threading.Thread
def test():
    pass
threading.Thread(target=test).start()
</code>
EDIT: I forgot to mention that I did <code>pip install -r requirements.txt</code> with the following requirements.txt:
<code>Django==1.9.7
django-appconf==1.0.2
django-autoslug==1.9.3
django-ckeditor==5.0.0
django-haystack==2.4.1
django-imagekit==3.2.7
django-modeltranslation==0.12
django-mptt==0.8.6
django-polymorphic==1.1.1
django-sek
