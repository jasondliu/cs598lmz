import socket
+import time
+import logging
+
+def main():
+	global default_log_level
+	global default_log_name
+	global default_log_format
+	global default_log_date_format
+	global default_log_max_bytes
+	global default_log_backup_count
+
+	logger = logging.getLogger()
+	formatter = logging.Formatter(default_log_format, default_log_date_format)
+	file_handler = logging.handlers.RotatingFileHandler(default_log_name, maxBytes = default_log_max_bytes, backupCount = default_log_backup_count)
+	file_handler.setFormatter(formatter)
+	stream_handler = logging.StreamHandler()
+	logger.addHandler(file_handler)
+	logger.addHandler(stream_handler)
+	logger.setLevel(default_log_level)
+
+	logger.info('Server start.')
+
+	host = '127.0.0
