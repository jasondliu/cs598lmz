import sys, threading
threading.Thread(target=lambda: get_ipython().run_line_magic('tb', '-x %qtconsole')).start()
print('To clear this cell, run:')
print('%clear')

#### Imports and constants ####
from lib.FileManager.workers.Drive.DriveDownloaderWorker import DriveDownloaderWorker

#### Processing ####
# Download all files from a folder and subfolders in a folder
def download_folder(self, folder_path, ignore_exts=None):
    self.logger.info("PID {} >>> {}".format(os.getpid(), self.request_id))
    self.logger.info("process_download_folder({}, ignore_exts={})".format(folder_path, ignore_exts))
    try:
        worker = DriveDownloaderWorker(self.logger, self.dm, self.request_id)
        worker.process(folder_path, ignore_exts, recursive=True)
    except Exception as e:
        self.logger.error("Error: {}\n{}".format(e, traceback.format_
