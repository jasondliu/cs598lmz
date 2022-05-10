import select
+
+class RPIO:
+    pwm_is_initialized = False
+    pwm_freq = 0
+    pwm_dma_channel = 0
+    pwm_range = 0
+    pwm_gpio_ms = 0
+    pwm_gpio_lsb = 0
+
+    def __init__(self):
+        pass
+
+    def gpio_function(self, gpio_id):
+        return "function"
+
+    def set_mode(self, mode_id):
+        pass
+
+    def setup(self, gpio_id, mode, initial=None):
+        pass
+
+    def input(self, gpio_id):
+        pass
+
+    def output(self, gpio_id, value):
+        pass
+
+    def input_pins(self, gpio_list):
+        return []
+
+    def output_pins(self, gpio_list, value):
+        pass
+
+    def add_inter
