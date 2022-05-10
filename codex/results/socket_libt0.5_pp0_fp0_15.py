import socket
+from pathlib import Path
+from datetime import datetime
+from time import sleep
+from threading import Thread
+from queue import Queue, Empty
+
+from tkinter import Tk, Frame, Text, Scrollbar, INSERT, END
+from tkinter.ttk import Button, Style
+from tkinter.messagebox import askokcancel
+
+
+class Chat(Frame):
+
+    def __init__(self, master):
+        super().__init__(master)
+        self.master = master
+        self.pack()
+
+        self.text = Text(self)
+        self.text.pack(side='left', fill='both', expand=True)
+        self.scroll = Scrollbar(self, command=self.text.yview)
+        self.text['yscrollcommand'] = self.scroll.set
+        self.scroll.pack(side='right', fill='y')
+
+        self.queue = Queue()
+        self.thread = Thread(target=self.loop, daemon
