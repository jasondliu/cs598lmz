import threading
# Test threading daemon
import time
import pprint

# TODO:
# 1. Add a way to check if a file is a duplicate before adding.
# 2. Add a way to check if a file is a duplicate before downloading.

class FileManager(threading.Thread):
    """Manages the downloading and uploading of files.
    """

    def __init__(self, peer_id, file_list, file_list_lock):
        """Constructor for FileManager.

        Args:
            peer_id: The id of the peer.
            file_list: A list of File objects.
            file_list_lock: A threading lock for the file_list.
        """
        super(FileManager, self).__init__()
        self.peer_id = peer_id
        self.file_list = file_list
        self.file_list_lock = file_list_lock
        self.daemon = True

    def run(self):
        """Starts the FileManager thread.
        """
        while True:
            self.file_list_lock.acquire()
            for
