import threading
threading.stack_size(1024*1024)

# The class that does it all
class the_class:
    def __init__(self, CONFIG):
        self.CONFIG = CONFIG

        # Internal settings
        self.logger = None
        self.input_csv_delimiter = None

        self.input_csv_file_path = None
        self.input_csv_file = None
        self.input_csv_file_iterator = None

        self.output_csv_file_path = None
        self.output_csv_file = None

        # Output CSV column names
        self.output_csv_column_names = None

        # The actual threads
        self.threads = []

        # Thread-safety locks
        self.lock_input = None
        self.lock_output = None

        # Output
        self.input_rows_read = 0
        self.input_rows_processed = 0
        self.output_rows_written = 0
        self.output_rows_failed = 0

        # Keep track of how far the program has progressed
        self.current
