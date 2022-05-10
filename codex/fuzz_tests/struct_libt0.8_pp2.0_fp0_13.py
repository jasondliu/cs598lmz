import _struct
+import sqlite3
+import time
+import _thread
+import threading 
+
+
+class Player:
+  def __init__(self, name, conn):
+    self.name = name
+    self.conn = conn
+    self.game = None
+    self.status = 0
+  
+  def in_game(self):
+    self.game.players.remove(self)
+    self.status = 0
+    self.game = None
+  
+
+class Game:
+  def __init__(self, creator):
+    self.id = int(time.time())
+    self.players = [creator]
+    self.creator = creator
+    self.open = True
+    self.running = False
+
+  def add_player(self, player):
+    if player in self.players:
+      return
+    self.players.append(player)
+  
+  def remove_player(self, player):
+    if not player in self.players:
+     
