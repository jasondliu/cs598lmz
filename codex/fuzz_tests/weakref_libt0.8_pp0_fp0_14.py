import weakref
+import re
+
+from threading import Lock
+
+
+_logger = logging.getLogger(__name__)
+
+
+class Parser(metaclass=abc.ABCMeta):
+	_parse_regex = re.compile(r'^\[(?P<timestamp>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\] \[(?P<thread>[A-Za-z_]+)\] (?P<log_type>[A-Z]+): (?P<message>[^\n]+)')
+
+	def __init__(self, config_path, start_offset=0):
+		self._config_path = config_path
+		self._start_offset = start_offset
+		self._parse_lock = Lock()
+		self._sinks = []
+		self._observers = []
+		
