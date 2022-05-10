import mmap
+import pywinusb.hid as hid
+import datetime
+import pyautogui
+
+#LavageHands
+
+apy="à"
+
+event2send={}
+event2send[hid.HID_EVENT_TYPE_OUTPUT]=()
+
+def hid_output(data):
+  event2send[hid.HID_EVENT_TYPE_OUTPUT] = data[:8]
+  keyboardHID.send_output_report(data)
+
+
+def handle_data(data):
+  string ="".join("%02X"%b for b in data)
+  print("Keypad PK201-D (TAG119): data = " + (string))
+  num=(string)
+  msg = num[14:22]
+  print("Numero digitado: "+msg)
+  #pyautogui.typewrite(msg,0.1)
+
+def handle_input(data):
+  print("Keypad PK201-D (TAG119): data =
