import weakref
+
+
+class Message:
+    def __init__(self, message):
+        self.message = message
+
+
+class MessageHandler:
+    def __init__(self):
+        self.listeners = []
+
+    def add_listener(self, listener):
+        self.listeners.append(listener)
+
+    def remove_listener(self, listener):
+        self.listeners.remove(listener)
+
+    def handle_message(self, message):
+        for listener in self.listeners:
+            listener.handle_message(message)
+
+
+class Listener:
+    def __init__(self, handler, name):
+        self.name = name
+        self.handler = handler
+        handler.add_listener(self)
+
+    def handle_message(self, message):
+        print(f'{self.name} got a message: {message.message}')
+
+
+def main():
+    handler = MessageHandler()
