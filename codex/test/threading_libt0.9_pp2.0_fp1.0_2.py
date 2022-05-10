import threading
threading.stack_size(10240000)
import time
from debugger_protocol import MeasData
from queue import Queue
from pylsl import StreamInfo, StreamOutlet
from RestAPI.IMU_client import IMU_client
from RestAPI.IMU_data_praser import IMU_data_praser

# from RestAPI.IMU_client import IMU_client



if __name__ == "__main__":
    port = 'COM3'
    IMU_ip = '192.168.1.221'
    server = IMU_data_praser(IMU_ip, port)
    server.build()
