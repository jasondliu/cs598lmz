import io
class File(io.RawIOBase):
    def __init__(self):
        self.current_page = 0
        self.page_content = ""
        self.cached_page_content = ""
        self.chars_in_current_page = 0

    def close(self):
        pass

    def write(self, x):
        raise NotImplementedError()

    def readable(self):
        return True

    def closed(self):
        return False

    def seekable(self):
        return False

    def writable(self):
        return False

    def _reset_content_retriever(self):
        self.current_page = 0
        self.page_content = ""
        self.chars_in_current_page = 0

    def _ensure_enough_content_available(self, chars_to_retrieve):
        if self.chars_in_current_page >= chars_to_retrieve:
            return

        page_count_to_retrieve =\
            (math.ceil((self.chars_in_current_page + chars_to_retrieve
