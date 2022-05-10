import threading
threading.stack_size(2**27)
from multiprocessing import Process

from my_config import settings
from utils import execute_cmd_line, run_cmd, get_cmd_output, get_logger, get_params_from_cmd, ask_question, run_cmd_with_output
from utils import get_cmd_output, get_params_from_cmd, create_failed_test_file
from crypto_tools import get_file_hash, get_folder_hash
from reporter import send_email
from settings import DEFAULT_EXECUTION_ID, DEFAULT_EMULATOR_BINARY_PATH, DEFAULT_EMULATOR_NAME, DEFAULT_DEVICE_NAME, DEFAULT_DEVICE_SERIAL, DEFAULT_REPORT_DESTINATION, DEFAULT_ADB_PORT
from settings import EMULATORS, MONKEYSERVER_RUNNING_TIME, BUILD_BRANCH, MONKEYSERVER_CMD_LINE, MONKEYSERVER_PUSH_FILE_CMD, MONKEYSERVER_PUSH_DIR_C
