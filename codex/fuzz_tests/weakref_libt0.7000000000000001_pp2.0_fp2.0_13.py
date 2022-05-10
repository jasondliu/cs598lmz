import weakref
+import time
+
+class AudioManager:
+    def __init__(self):
+        self._sounds = {}
+        self._playing_sounds = set()
+        self._playing_sound_refs = set()
+
+    def add_sound(self, name, sound):
+        if name in self._sounds:
+            raise Exception("Sound named '{}' already exists".format(name))
+        self._sounds[name] = sound
+
+    def get_sound(self, name):
+        if name not in self._sounds:
+            raise Exception("Sound named '{}' does not exist".format(name))
+        return self._sounds[name]
+
+    def play_sound(self, sound, loop=False):
+        s = sound.play(loop)
+        self._playing_sounds.add(s)
+        self._playing_sound_refs.add(weakref.ref(s))
+        return s
+
+    def stop_sound(self, sound):
