import threading
threading.stack_size(2**28)

from Hdl_stream import hdl_stream, config_stream
from Hdl_reader import hdl_Reader
from Hdl_writer import hdl_writer
from Hdl_read_writer import hdl_read_writer
from Hdl_tb_helper import hdl_logger, hdl_tb_helper, hdl_tb_helper_obj, hdl_tb_helper_register, hdl_tb_helper_mem, vcd_generator
from Hdl_net import hdl_net
from Hdl_net_connector import hdl_net_connector
from Hdl_stream_utils import hdl_stream_utils, hdl_stream_shrinker, hdl_stream_converter
from Hdl_setter_getter_gen import hdl_setter_getter_gen
from Hdl_functions import hdl_functions
from Hdl_scope import hdl_scope
from Hdl_task import hdl_task
from Hdl_simulator import hdl_
