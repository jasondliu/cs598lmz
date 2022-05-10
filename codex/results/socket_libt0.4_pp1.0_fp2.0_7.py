import socket
+from threading import Thread
+
+def receive():
+    while True:
+        try:
+            message = client_socket.recv(BUFSIZ).decode("utf8")
+            msg_list.insert(tkinter.END, message)
+        except OSError:  # Possibly client has left the chat.
+            break
+
+
+def send(event=None):  # event is passed by binders.
+    """Handles sending of messages."""
+    message = my_msg.get()
+    my_msg.set("")  # Clears input field.
+    client_socket.send(bytes(message, "utf8"))
+    if message == "{quit}":
+        client_socket.close()
+        top.quit()
+
+
+def on_closing(event=None):
+    """This function is to be called when the window is closed."""
+    my_msg.set("{quit}")
+    send()
+
+top = tkinter.Tk()
+
