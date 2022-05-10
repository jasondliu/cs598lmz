import gc, weakref
+
+class Person:
+    def __init__(self, name, surname, number):
+        self.name = name
+        self.surname = surname
+        self.number = number
+
+    def __repr__(self):
+        return f"{self.name} {self.surname} {self.number}"
+
+
+person = Person("Jan", "Nowak", "1234")
+
+print(person)
+
+person = None
+
+gc.collect()
+
+print(person)
+
+
+# lista referencyjna
+
+person = Person("Jan", "Nowak", "1234")
+
+print(person)
+
+weak_person = weakref.ref(person)
+
+person = None
+
+gc.collect()
+
+print(weak_person)
+print(weak_person())
+
+
+
+
+

