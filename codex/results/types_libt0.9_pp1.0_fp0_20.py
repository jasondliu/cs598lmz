import types
types.ClassType

c:\python24>python
Python 2.4.1 (#65, Mar 30 2005, 09:13:57) [MSC v.1310 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Ah ha, class type is gone
...
>>> import types
>>> types.ClassType
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
AttributeError: 'module' object has no attribute 'ClassType'
>>>

c:\python24>
""",
u"""
jean-pierre
""" ),

(u"""
Un appel de Sys.path avec un argument semble crasher le moteur Python.

Voici le message d'erreur :
 AttributeError: 'module' object has no attribute '_set_path'
Ce que je ne comprend pas c'est pourquoi il m'indique l'attribut _set_path alors que je lui ai transmis la chaîne 'set_path'.
