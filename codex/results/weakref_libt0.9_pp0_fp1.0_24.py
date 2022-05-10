import weakref
+
+
+class User:
+    users = weakref.WeakValueDictionary()
+
+    def __init__(self, name):
+        self._name = name
+        User.users[name] = self
+        print("(New User: {})".format(name))
+
+    def sendmsg(self, msg):
+        print("{} tells: {}".format(self._name, msg))
+
+    def receivemsg(self, sender, msg):
+        print("{} receives a message '{}' from {}.".format(self._name, msg, sender))
+
+
+def send(sender, reciver, name):
+    reciver = User.users[reciver]
+    reciver.receivemsg(sender, name)
+
+
+if __name__ == "__main__":
+    print("Create new users")
+    a = User("Alice")
+    b = User("Bob")
+    c = User("Charlie")
+    print()
+
+    print("
