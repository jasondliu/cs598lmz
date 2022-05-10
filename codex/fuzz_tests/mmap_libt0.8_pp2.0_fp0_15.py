import mmap
+
+
+def get_supported_cards():
+    """ Retrieve supported cards from cards.xml file """
+    xml = ""
+    try:
+        with open("cards.xml", "rb") as f:
+            xml = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+    except EnvironmentError:
+        print("cards.xml not found")
+        sys.exit(0)
+
+    root = ET.fromstring(xml)
+    cards = root.findall(".//card")
+
+    supported_cards = {}
+    for x in cards:
+        if x.find("vendor") is not None:
+            if x.find("model") is not None:
+                supported_cards[x.find("vendor").text + " " + x.find("model").text] = {
+                    "section": x.find("section").text,
+                    "name": x.find("name").text,
+                    "vendor": x.find("vendor").
