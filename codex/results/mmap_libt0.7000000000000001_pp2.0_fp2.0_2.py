import mmap
+
+# Constants
+BASE_ADDR = 0x0
+INPUT_BYTE_SIZE = 8
+OUTPUT_BYTE_SIZE = 8
+
+# Check args
+if len(sys.argv) != 2:
+    print("Usage: ./blink_led.py <bitstream.bin>")
+    sys.exit(1)
+
+# Open the bitstream
+file_name = sys.argv[1]
+print("Opening bitstream " + file_name)
+bitstream_fd = open(file_name, "rb")
+bitstream_fd.seek(0,2) # Seek to the end
+file_size = bitstream_fd.tell()
+bitstream_fd.seek(0,0) # Seek back to the beginning
+
+# Open the memory device
+print("Opening /dev/mem")
+mem_fd = open("/dev/mem", "rb+")
+
+# Memory map the memory device
+print("Mapping memory device to memory")
+mem_map =
