import mmap
import struct
import time

_CONFIG_FILE_PATH = '../../../epics/IOC/autoconf/simDetectorConfig/'


class MockConfig():
    """A class to mock config files to conduct testing on other modules"""


    def __init__(self):
        self.config_files = {}    # (str projectContent): {str: str} [projectID]
        self.numberOfBoards = 3   # The hard-coded number of boards
        self.defaultMboards = {}
        self.defaultMboard = 'NI-6674'
        self.adc_rate = '500 MHz'


    def _get_config_file_path(self, project, project_activity):
        """Method to get all of the paths for all of the config files

        @param project (str):           The project name
        @param project_activity (str):  The project activity name

        returns an array of strings, where the string is the the absolute path to the config file
        """

        proj_filename = 'project.cfg'
        projact_filename =
